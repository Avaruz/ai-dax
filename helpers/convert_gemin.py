import re
import json
import argparse # Importado para manejar argumentos de línea de comandos
import sys # Importado para sys.exit

def parse_tdml_to_json(tdml_content):
    """
    Convierte una cadena de contenido TDML a una cadena JSON.
    Este es un parser inicial y puede necesitar refinamientos
    para manejar todos los casos de la sintaxis TDML.
    """
    lines = tdml_content.splitlines()
    model_data = {"tables": []}
    current_table_dict = None
    current_item_details = {}
    capturing_block_for = None 
    block_buffer = []
    block_start_indent = -1
    expected_block_terminator = None

    table_regex = re.compile(r"^\s*table\s+((?:'[^']+')|(?:[^\s]+))\s*$")
    column_regex = re.compile(r"^\s*column\s+((?:'[^']+')|(?:[^\s]+))\s*(?:=\s*)?$")
    measure_regex = re.compile(r"^\s*measure\s+((?:'[^']+')|(?:[^\s]+))\s*=\s*$")
    partition_regex = re.compile(r"^\s*partition\s+([^\s]+)\s*=\s*m\s*$")
    property_regex = re.compile(r"^\s*([a-zA-Z0-9_]+)\s*:\s*(.*)$")
    annotation_regex = re.compile(r"^\s*annotation\s+([a-zA-Z0-9_]+)\s*=\s*(.*)$")
    changed_property_regex = re.compile(r"^\s*changedProperty\s*=\s*(.*)$")
    extended_property_start_regex = re.compile(r"^\s*extendedProperty\s+([a-zA-Z0-9_]+)\s*=\s*$")
    source_start_regex = re.compile(r"^\s*source\s*=\s*$")

    def clean_name(name):
        return name.strip().strip("'")

    def add_detail(target_dict, key, value):
        if key in target_dict:
            if not isinstance(target_dict[key], list):
                target_dict[key] = [target_dict[key]]
            target_dict[key].append(value)
        else:
            target_dict[key] = value
            
    def finalize_current_item(table_dict_ref, item_details_ref, section_type):
        # Corrige: agrega si hay 'name' en item_details_ref, aunque no tenga más propiedades
        if not table_dict_ref or not section_type:
            return
        if section_type == 'column' and 'name' in item_details_ref:
            table_dict_ref.setdefault('columns', []).append(dict(item_details_ref))
        elif section_type == 'measure' and 'name' in item_details_ref:
            table_dict_ref.setdefault('measures', []).append(dict(item_details_ref))
        elif section_type == 'partition' and 'name' in item_details_ref:
            table_dict_ref.setdefault('partitions', []).append(dict(item_details_ref))
        item_details_ref.clear()

    current_section_type = None

    for line in lines:
        stripped_line = line.strip()
        current_indent = len(line) - len(line.lstrip())

        # Si estamos capturando un bloque y detectamos una nueva tabla/columna/medida/partición, forzamos el cierre del bloque
        if capturing_block_for:
            is_new_major_definition = (table_regex.match(line) or column_regex.match(line) or measure_regex.match(line) or partition_regex.match(line))
            if is_new_major_definition:
                # Forzar cierre del bloque anterior
                content = "\n".join(block_buffer)
                if not current_item_details:
                    current_item_details = {}
                current_item_details[capturing_block_for] = content.strip()
                capturing_block_for = None
                block_buffer = []
                expected_block_terminator = None
            else:
                is_new_major_definition = (table_regex.match(line) and current_indent <= block_start_indent) or \
                                          (column_regex.match(line) and current_indent <= block_start_indent) or \
                                          (measure_regex.match(line) and current_indent <= block_start_indent) or \
                                          (partition_regex.match(line) and current_indent <= block_start_indent)

                is_sibling_or_parent_property = False
                if not expected_block_terminator: 
                    if property_regex.match(line) or annotation_regex.match(line) or \
                       changed_property_regex.match(line) or extended_property_start_regex.match(line) or \
                       source_start_regex.match(line):
                        if current_indent <= block_start_indent: 
                            is_sibling_or_parent_property = True
                if expected_block_terminator == '}' and stripped_line == '}' and current_indent == block_start_indent:
                    block_buffer.append(stripped_line)
                    content = "\n".join(block_buffer)
                    try:
                        if not current_item_details: current_item_details = {}
                        current_item_details[capturing_block_for] = json.loads(content)
                    except Exception as e:
                        print(f"Warning: Could not parse JSON block for {capturing_block_for}: {content[:100]}... {e}")
                        if not current_item_details: current_item_details = {}
                        current_item_details[capturing_block_for] = content 
                    capturing_block_for = None
                    block_buffer = []
                    expected_block_terminator = None
                elif not expected_block_terminator and block_start_indent != -1 and (current_indent < block_start_indent or is_new_major_definition or is_sibling_or_parent_property):
                    content = "\n".join(b.strip() for b in block_buffer) 
                    if not current_item_details: current_item_details = {}
                    current_item_details[capturing_block_for] = content.strip()
                    capturing_block_for = None
                    block_buffer = []
                else: 
                    block_buffer.append(line) 
                    continue 
        
        match_tbl = table_regex.match(line)
        if match_tbl:
            if current_table_dict: 
                finalize_current_item(current_table_dict, current_item_details, current_section_type)
                model_data["tables"].append(current_table_dict)
            table_name = clean_name(match_tbl.group(1))
            current_table_dict = {"name": table_name, "properties": {}, "annotations": [], "columns": [], "measures": [], "partitions": []}
            current_item_details.clear() 
            current_section_type = 'table'
            print(f"Processing Table: {table_name}")
            continue

        match_col = column_regex.match(line)
        if match_col and current_table_dict:
            finalize_current_item(current_table_dict, current_item_details, current_section_type)
            col_name = clean_name(match_col.group(1))
            current_item_details = {"name": col_name, "properties": {}, "annotations": []}
            current_section_type = 'column'
            if line.strip().endswith("="): 
                capturing_block_for = 'expression'
                block_start_indent = current_indent + 1 
                block_buffer = []
                expected_block_terminator = None
            print(f"  Processing Column: {col_name}")
            continue

        match_measure = measure_regex.match(line)
        if match_measure and current_table_dict:
            finalize_current_item(current_table_dict, current_item_details, current_section_type)
            measure_name = clean_name(match_measure.group(1))
            current_item_details = {"name": measure_name, "properties": {}, "annotations": []}
            current_section_type = 'measure'
            capturing_block_for = 'expression' 
            block_start_indent = current_indent + 1
            block_buffer = []
            expected_block_terminator = None
            print(f"  Processing Measure: {measure_name}")
            continue

        match_partition = partition_regex.match(line)
        if match_partition and current_table_dict:
            finalize_current_item(current_table_dict, current_item_details, current_section_type)
            partition_name = clean_name(match_partition.group(1))
            current_item_details = {"name": partition_name, "properties": {}, "annotations": []}
            current_section_type = 'partition'
            print(f"  Processing Partition: {partition_name}")
            continue

        active_target_for_properties = current_item_details if current_section_type in ['column', 'measure', 'partition'] else \
                                     current_table_dict if current_table_dict and current_section_type == 'table' else None
        
        if not active_target_for_properties:
            continue

        prop_dict_location = active_target_for_properties.setdefault('properties', {})

        match_src_start = source_start_regex.match(line)
        if match_src_start and current_section_type == 'partition':
            capturing_block_for = 'source_m_query'
            block_start_indent = current_indent + 1 
            block_buffer = []
            expected_block_terminator = None 
            print(f"    Starting M Query block for partition {current_item_details.get('name')}")
            continue
            
        match_ext_prop_start = extended_property_start_regex.match(line)
        if match_ext_prop_start:
            prop_name = clean_name(match_ext_prop_start.group(1))
            capturing_block_for = prop_name 
            block_start_indent = current_indent 
            block_buffer = []
            expected_block_terminator = '}' 
            if stripped_line.endswith("{"):
                block_buffer.append("{")
            print(f"    Starting Extended Property block: {prop_name}")
            continue

        match_prop = property_regex.match(line)
        if match_prop:
            key, value = clean_name(match_prop.group(1)), match_prop.group(2).strip()
            if current_section_type == 'table' and key in ['lineageTag', 'description']:
                add_detail(current_table_dict, key, value)
            else:
                add_detail(prop_dict_location, key, value)
            continue

        match_annot = annotation_regex.match(line)
        if match_annot:
            annot_list_location = active_target_for_properties.setdefault('annotations', [])
            key, value_str = clean_name(match_annot.group(1)), match_annot.group(2).strip()
            if value_str.startswith("{") and value_str.endswith("}"):
                try:
                    parsed_value = json.loads(value_str)
                    annot_list_location.append({key: parsed_value})
                except Exception as e:
                    print(f"[WARN] Could not parse annotation JSON for {key}: {e}. Storing as string.")
                    annot_list_location.append({key: value_str})
            elif value_str == "{":                 
                capturing_block_for = key 
                block_start_indent = current_indent 
                block_buffer = ["{"]
                expected_block_terminator = '}'
                print(f"    Starting Annotation JSON block: {key}")
            else:
                annot_list_location.append({key: value_str})
            capturing_block_for = None  # Asegura que no se quede atascado
            continue
            
        match_changed = changed_property_regex.match(line)
        if match_changed:
            value = match_changed.group(1).strip()
            add_detail(prop_dict_location, 'changedProperty', value)
            continue

    # Al final del archivo, asegurar que el último item se agregue
    if current_table_dict:
        finalize_current_item(current_table_dict, current_item_details, current_section_type)
        model_data["tables"].append(current_table_dict)

    # Limpieza final
    for table in model_data["tables"]:
        for key_list_name in ['columns', 'measures', 'partitions', 'annotations']:
            if key_list_name in table and not table[key_list_name]:
                del table[key_list_name]
        if 'properties' in table and not table['properties']:
            del table['properties']
        for item_type in ['columns', 'measures', 'partitions']:
            for item in table.get(item_type, []):
                if 'properties' in item and not item['properties']:
                    del item['properties']
                if 'annotations' in item and not item['annotations']:
                    del item['annotations']

    return json.dumps(model_data, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convierte un archivo TDML a JSON.")
    parser.add_argument("-i", "--input", help="Ruta al archivo TDML de entrada.", required=True) # Hacer el input obligatorio
    parser.add_argument("-o", "--output", help="Ruta al archivo JSON de salida. Si no se especifica, se imprime en consola.")

    args = parser.parse_args()

    tdml_content_to_parse = None # Inicializar a None

    if args.input: # Siempre será verdadero debido a required=True, pero mantenemos la estructura
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                tdml_content_to_parse = f.read()
            print(f"Archivo TDML cargado desde: {args.input}")
        except FileNotFoundError:
            print(f"Error: El archivo de entrada '{args.input}' no fue encontrado.")
            sys.exit(1) # Salir del script si el archivo no se encuentra
        except Exception as e:
            print(f"Error al leer el archivo de entrada '{args.input}': {e}.")
            sys.exit(1) # Salir del script en caso de otros errores de lectura
    
    # Si tdml_content_to_parse sigue siendo None, algo salió mal con la lógica de argparse o required=True
    # (aunque con required=True, argparse debería haber salido antes si no se proveyó -i)
    if tdml_content_to_parse is None:
        print("Error: No se pudo obtener el contenido TDML para parsear. Asegúrese de proveer un archivo de entrada con -i.")
        sys.exit(1)

    parsed_json_result = parse_tdml_to_json(tdml_content_to_parse)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as outfile:
                outfile.write(parsed_json_result)
            print(f"Resultado JSON guardado en: {args.output}")
        except Exception as e:
            print(f"Error al guardar el archivo de salida '{args.output}': {e}")
            print("\n--- JSON Result (Consola) ---")
            print(parsed_json_result)
    else:
        print("\n--- JSON Result (Consola) ---")
        print(parsed_json_result)

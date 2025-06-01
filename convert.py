import re
import json
from pathlib import Path

# Archivo de entrada
ARCHIVO_TDML = "TDML_Modelo.txt"

# Leer el archivo TDML
with open(ARCHIVO_TDML, "r", encoding="utf-8") as f:
    contenido = f.read()

# Expresiones regulares para extraer tablas y columnas
tabla_regex = re.compile(r"table '([^']+)'[\s\S]+?column", re.MULTILINE)
columna_regex = re.compile(r"column ([^\n=]+)[\s\S]+?dataType: ([^\n]+)", re.MULTILINE)

# Resultado JSON y Markdown
modelo_json = []
MODELO_MD = "# Modelo de Datos (Extraído de TDML)\n\n"

# Procesar cada tabla
for tabla in re.finditer(r"table '([^']+)'[\s\S]+?partition", contenido):
    nombre_tabla = tabla.group(1)
    bloque_tabla = tabla.group(0)

    columnas = []
    md_tabla = f"## Tabla: {nombre_tabla}\n\n"
    md_tabla += "| Columna | Tipo de Dato |\n|---------|---------------|\n"

    for match in columna_regex.finditer(bloque_tabla):
        nombre_col = match.group(1).strip("'")
        tipo_dato = match.group(2).strip()
        columnas.append({"nombre": nombre_col, "tipo": tipo_dato})
        md_tabla += f"| {nombre_col} | {tipo_dato} |\n"

    modelo_json.append({"tabla": nombre_tabla, "columnas": columnas})
    MODELO_MD += md_tabla + "\n"

# Guardar archivos
Path("Modelo_TDML.md").write_text(MODELO_MD, encoding="utf-8")
Path("Modelo_TDML.json").write_text(json.dumps(modelo_json, indent=2), encoding="utf-8")

print("Archivos generados: Modelo_TDML.md y Modelo_TDML.json")

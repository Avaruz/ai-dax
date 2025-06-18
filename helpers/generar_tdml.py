import json

def generar_documentacion_markdown(archivo_json, archivo_salida):
    """
    Genera documentación markdown a partir de un archivo JSON con estructura de tablas
    
    Args:
        archivo_json (str): Ruta del archivo JSON de entrada
        archivo_salida (str): Ruta del archivo markdown de salida
    """
    
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        # Crear el contenido markdown
        markdown_content = "# Documentación del Modelo de Datos\n\n"
        
        # Procesar cada tabla
        for tabla in datos:
            nombre_tabla = tabla.get('table', 'Sin nombre')
            columnas = tabla.get('columns', [])
            
            # Agregar separador y nombre de tabla
            markdown_content += f"Tabla: {nombre_tabla}\n"
            markdown_content += f"------------------------------\n"
            
            # Agregar columnas
            for columna in columnas:
                nombre_columna = columna.get('name', 'Sin nombre')
                tipo_dato = columna.get('dataType')                
                if tipo_dato:
                    markdown_content += f"- {nombre_columna} ({tipo_dato})\n"
                else:
                    markdown_content += f"- {nombre_columna}\n"
            
            # Agregar línea en blanco entre tablas
            markdown_content += "\n"
        
        # Escribir el archivo markdown
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✅ Documentación generada exitosamente: {archivo_salida}")
        print(f"📊 Total de tablas procesadas: {len(datos)}")
        
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {archivo_json}")
    except json.JSONDecodeError:
        print(f"❌ Error: El archivo {archivo_json} no tiene un formato JSON válido")
    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")

def mostrar_resumen_modelo(archivo_json):
    """
    Muestra un resumen del modelo de datos
    
    Args:
        archivo_json (str): Ruta del archivo JSON
    """
    
    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        print("📋 RESUMEN DEL MODELO DE DATOS")
        print("=" * 50)
        
        total_columnas = 0
        tipos_datos = {}
        
        for tabla in datos:
            nombre_tabla = tabla.get('table', 'Sin nombre')
            columnas = tabla.get('columns', [])
            num_columnas = len(columnas)
            total_columnas += num_columnas
            
            print(f"📄 {nombre_tabla}: {num_columnas} columnas")
            
            # Contar tipos de datos
            for columna in columnas:
                tipo_dato = columna.get('dataType', 'null')
                tipos_datos[tipo_dato] = tipos_datos.get(tipo_dato, 0) + 1
        
        print("\n📊 ESTADÍSTICAS:")
        print(f"   Total de tablas: {len(datos)}")
        print(f"   Total de columnas: {total_columnas}")
        print(f"   Promedio de columnas por tabla: {total_columnas / len(datos):.1f}")
        
        print("\n🏷️  TIPOS DE DATOS:")
        for tipo, cantidad in sorted(tipos_datos.items()):
            print(f"   {tipo}: {cantidad} columnas")
            
    except Exception as e:
        print(f"❌ Error al mostrar resumen: {str(e)}")

def generar_documentacion_con_filtros(archivo_json, archivo_salida, filtro_tablas=None):
    """
    Genera documentación con filtros opcionales
    
    Args:
        archivo_json (str): Ruta del archivo JSON
        archivo_salida (str): Ruta del archivo markdown de salida
        filtro_tablas (list): Lista de nombres de tablas a incluir (None para todas)
    """
    
    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        # Filtrar tablas si se especifica
        if filtro_tablas:
            datos = [tabla for tabla in datos if tabla.get('table') in filtro_tablas]
            print(f"🔍 Aplicando filtro: {len(datos)} tablas seleccionadas")
        
        markdown_content = "# Documentación del Modelo de Datos\n\n"
        
        if filtro_tablas:
            markdown_content += f"*Documentación filtrada - Tablas incluidas: {', '.join(filtro_tablas)}*\n\n"
        
        for tabla in datos:
            nombre_tabla = tabla.get('table', 'Sin nombre')
            columnas = tabla.get('columns', [])
            
            markdown_content += f"------------------------------\n"
            markdown_content += f"Tabla: {nombre_tabla}\n"
            markdown_content += f"------------------------------\n"
            
            for columna in columnas:
                nombre_columna = columna.get('name', 'Sin nombre')
                tipo_dato = columna.get('dataType')
                
                if tipo_dato:
                    markdown_content += f"- {nombre_columna} ({tipo_dato})\n"
                else:
                    markdown_content += f"- {nombre_columna}\n"
            
            markdown_content += "\n"
        
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✅ Documentación generada: {archivo_salida}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

# Ejemplo de uso principal
if __name__ == "__main__":
    # Configuración de archivos
    archivo_entrada = "data\\modelo_reducido.json"
    archivo_salida = "data\\documentacion_modelo.md"
    
    print("🚀 Generador de Documentación de Modelo de Datos")
    print("=" * 55)
    
    # Mostrar resumen del modelo
    print("\n1️⃣ Analizando modelo de datos...")
    mostrar_resumen_modelo(archivo_entrada)
    
    # Generar documentación completa
    print("\n2️⃣ Generando documentación completa...")
    generar_documentacion_markdown(archivo_entrada, archivo_salida)
    
    # Ejemplo: Generar documentación solo para tablas específicas
    print("\n3️⃣ Ejemplo: Documentación filtrada...")
    tablas_importantes = ["Ventas Mensuales", "Producto Compañía", "Área Terapéutica"]
    generar_documentacion_con_filtros(
        archivo_entrada, 
        "documentacion_filtrada.md", 
        tablas_importantes
    )
    
    print("\n✨ Proceso completado!")

# Función adicional para usar desde otros scripts
def convertir_json_a_markdown(json_data, incluir_tipos=True):
    """
    Convierte datos JSON directamente a string markdown
    
    Args:
        json_data (list): Lista de diccionarios con estructura de tablas
        incluir_tipos (bool): Si incluir tipos de datos en la salida
    
    Returns:
        str: Contenido markdown generado
    """
    
    markdown_content = "# Documentación del Modelo de Datos\n\n"
    
    for tabla in json_data:
        nombre_tabla = tabla.get('table', 'Sin nombre')
        columnas = tabla.get('columns', [])
        
        markdown_content += f"------------------------------\n"
        markdown_content += f"Tabla: {nombre_tabla}\n"
        markdown_content += f"------------------------------\n"
        
        for columna in columnas:
            nombre_columna = columna.get('name', 'Sin nombre')
            tipo_dato = columna.get('dataType')
            
            if incluir_tipos and tipo_dato:
                markdown_content += f"- {nombre_columna} ({tipo_dato})\n"
            else:
                markdown_content += f"- {nombre_columna}\n"
        
        markdown_content += "\n"
    
    return markdown_content
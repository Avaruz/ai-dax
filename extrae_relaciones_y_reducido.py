import json

with open("modelo.json", encoding="utf-8") as f:
    data = json.load(f)

# 1. Extraer relaciones de annotation PBI_QueryRelationships
relaciones = []
for tabla in data.get("tables", []):
    for col in tabla.get("columns", []):
        for ann in col.get("annotations", []):
            if "PBI_QueryRelationships" in ann:
                relaciones.append({
                    "tabla": tabla["name"],
                    "columna": col["name"],
                    "relacion": ann["PBI_QueryRelationships"]
                })

# 2. Modelo reducido de columnas
modelo_reducido = []
for tabla in data.get("tables", []):
    columnas = []
    for col in tabla.get("columns", []):
        props = col.get("properties", {})
        columnas.append({
            "name": col.get("name"),
            "dataType": props.get("dataType"),
            "formatString": props.get("formatString"),
            "sourceColumn": props.get("sourceColumn")
        })
    modelo_reducido.append({
        "table": tabla.get("name"),
        "columns": columnas
    })

# Guardar resultados
with open("relaciones.json", "w", encoding="utf-8") as f:
    json.dump(relaciones, f, indent=2, ensure_ascii=False)

with open("modelo_reducido.json", "w", encoding="utf-8") as f:
    json.dump(modelo_reducido, f, indent=2, ensure_ascii=False)

print("Listo: relaciones.json y modelo_reducido.json generados.")

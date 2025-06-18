import json

with open("data\\modelo.json", encoding="utf-8") as f:
    data = json.load(f)

# 2. Modelo reducido de columnas
modelo_reducido = []
for tabla in data.get("tables", []):
    columnas = []
    for col in tabla.get("columns", []):
        props = col.get("properties", {})
        columnas.append({
            "name": col.get("name"),
            "dataType": props.get("dataType")
            })
    modelo_reducido.append({
        "table": tabla.get("name"),
        "columns": columnas
    })

# Guardar resultados
with open("data\\modelo_reducido.json", "w", encoding="utf-8") as f:
    json.dump(modelo_reducido, f, indent=2, ensure_ascii=False)

print("Listo: relaciones.json y modelo_reducido.json generados.")

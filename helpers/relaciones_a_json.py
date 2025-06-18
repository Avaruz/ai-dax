import re
import json

relaciones = []
with open("relaciones.txt", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if not linea or not linea.startswith("Relacion entre:"):
            continue
        # Ejemplo: Relacion entre: 'Ventas Mensuales'[IdCanal]  de Varios a 1 'Canal'[IdCanal]
        m = re.match(r"Relacion entre: '?([^']+)'?\[([^\]]+)\]\s+de\s+([\w\s]+)\s+a\s+([\w\s]+) '?([^']+)'?\[([^\]]+)\]", linea)
        if m:
            origen_tabla = m.group(1).strip()
            origen_col = m.group(2).strip()
            cardinalidad_origen = m.group(3).strip()
            cardinalidad_destino = m.group(4).strip()
            destino_tabla = m.group(5).strip()
            destino_col = m.group(6).strip()
            relaciones.append({
                "from_table": origen_tabla,
                "from_column": origen_col,
                "from_cardinality": cardinalidad_origen,
                "to_table": destino_tabla,
                "to_column": destino_col,
                "to_cardinality": cardinalidad_destino
            })
        else:
            relaciones.append({"raw": linea})

with open("relaciones_estructurado.json", "w", encoding="utf-8") as f:
    json.dump(relaciones, f, indent=2, ensure_ascii=False)

print("Listo: relaciones_estructurado.json generado.")

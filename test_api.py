import requests
import json

API_URL = "http://localhost:8000/dax-query"
TOKEN = "mysecrettoken"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

data = {
    "question": "¿Cuál es el total de ventas por país?"
}

response = requests.post(API_URL, json=data, headers=headers)

try:
    response.raise_for_status()
    result = response.json()
    # Guardar la respuesta en un archivo JSON
    with open("respuesta.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    assert "Question" in result or "question" in result, "Falta el campo 'question' en la respuesta."
    assert "DAX" in result or "dax_code" in result, "Falta el campo 'dax_code' en la respuesta."
    print("Respuesta válida y guardada en respuesta.json:\n", result)
except Exception as e:
    print("Error al validar la respuesta:", e)
    print("Respuesta recibida:", response.text)

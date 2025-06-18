from fastapi import FastAPI, Request, HTTPException, status, Header
from pydantic import BaseModel
from flow import DAXAssistant
import os
import re

app = FastAPI()

# Token de ejemplo, puedes cambiarlo por uno seguro o cargarlo de una variable de entorno
VALID_BEARER_TOKEN = os.getenv("DAX_API_TOKEN", "mysecrettoken")
DEFAULT_MODELO_DATOS = os.path.join("data", "modelo_datos.json")
DEFAULT_RELACIONES = os.path.join("data", "relaciones.json")

class DAXRequest(BaseModel):
    question: str

@app.post("/dax-query")
async def dax_query(req: DAXRequest, Authorization: str = Header(None)):
    # Validar token Bearer
    if not Authorization or not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid Authorization header")
    token = Authorization.split(" ", 1)[1]
    if token != VALID_BEARER_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    asistente = DAXAssistant()
    consulta = asistente.generate_dax_query(
        user_question=req.question,
        model_data_path=DEFAULT_MODELO_DATOS,
        relations_path=DEFAULT_RELACIONES
    )
    # Limpiar formato markdown y encabezados
    if isinstance(consulta, str):
        consulta = re.sub(r"^```dax[\r\n]+|^```[\r\n]+|```$", "", consulta, flags=re.MULTILINE).strip()
        lines = consulta.splitlines()
        cleaned = []
        for line in lines:
            if line.strip() in ("", "DAX", "---"): continue
            cleaned.append(line)
        consulta = "\n".join(cleaned).strip()
    return {
        "DAX": consulta,
        "Question": req.question
    }

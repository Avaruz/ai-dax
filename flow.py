"""
Este script de Python convierte un flujo de Langflow en una aplicación ejecutable.
La lógica está encapsulada en una clase 'DAXAssistant' para mayor modularidad y reutilización.

Funcionalidad:
1. Carga la configuración del modelo y las relaciones de archivos JSON externos.
2. Construye un prompt de sistema detallado para instruir al modelo de IA.
3. Utiliza el modelo generativo de Google (Gemini) para generar consultas DAX.
4. Permite la entrada de preguntas a través de la línea de comandos para facilitar las pruebas.
"""

import os
import json
import argparse
from typing import Dict, Any

# LangChain y dependencias de Google
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.exceptions import LangChainException

# Para cargar variables de entorno de forma segura desde un archivo .env
from dotenv import load_dotenv

class DAXAssistant:
    """
    Un asistente de IA que genera consultas DAX a partir de un modelo de datos
    y una pregunta en lenguaje natural.
    """

    # Plantilla del prompt de sistema extraída del flujo de Langflow.
    SYSTEM_PROMPT_TEMPLATE = """
Propósito:
Eres un asistente experto en DAX y Microsoft Power BI.

Tarea:
Tu tarea es analizar el siguiente esquema de modelo de datos y generar consultas DAX precisas basadas en las preguntas del usuario.

Contexto:
- Asegúrate de que la sintaxis sea correcta y verifica que la consulta sea correcta, para eso usa tu base de conocimiento DAX Functions Reference.
- Utiliza las tablas y columnas exactamente como se definen en el esquema, usa el conocimiento Modelo de datos de tu base de conocimiento.
- Envuelve los nombres de tablas con comillas simples si contienen espacios y las columnas con corchetes, ejemplo 'Marca'[Marca]
- Evita usar espacios en las variables usa _ en vez de espacios y da los nombres de las variables en español.
- Asume como indicador de Ventas, el campo [USD] de la tabla 'Ventas Mensuales'
- Usa la tabla 'Período a Analizar' para filtrar las fechas de las consultas DAX.
- La tabla principal de las Ventas es 'Ventas Mensuales'
- Usa [UNSTD] para las Unidades
- Respeta los acentos de los nombres del modelo como ser País
- Da los datos sin decimales
- Proporciona ÚNICAMENTE la consulta DAX como respuesta, sin explicaciones adicionales a menos que se te pida explícitamente
- Agrega este filtro siempre IdCanal por {{"LIC", "EXT", "INS", "LOC"}}
- TA se refiere a Área Terapéutica
- No uses ñ para los nombres de las variables ya que DAX no lo soporta
- Cuando te hable de Molécula me refiero a SubFamilia

Formato:
- Analiza el modelo de datos.
- Revisa las el archivo [Preguntas y Respuestas DAX Copilot Studio.txt] para ver como responder.

Modelo de datos:
{modelo_datos}

Relaciones:
{relaciones}
"""

    def __init__(self, model_name: str = "gemini-2.5-pro-preview-03-25", temperature: float = 0.72):
        """
        Inicializa el asistente, carga la clave de API y configura el modelo de lenguaje.
        """
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("No se encontró la GOOGLE_API_KEY. Asegúrate de que esté en tu archivo .env o configurada como variable de entorno.")
        
        self.model = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=temperature,
            google_api_key=api_key
        )
        print(f"Modelo '{model_name}' inicializado correctamente.")

    def _load_json_as_string(self, file_path: str) -> str:
        """
        Carga un archivo JSON y lo devuelve como una cadena de texto formateada.
        Args:
            file_path: La ruta al archivo JSON.
        Returns:
            Una cadena con el contenido del JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return json.dumps(data, indent=2, ensure_ascii=False)
        except FileNotFoundError:
            print(f"Advertencia: El archivo '{file_path}' no fue encontrado. Se usará un objeto JSON vacío.")
            return "{}"
        except json.JSONDecodeError:
            print(f"Advertencia: Error al decodificar JSON en '{file_path}'. Se usará un objeto JSON vacío.")
            return "{}"

    def generate_dax_query(self, user_question: str, model_data_path: str, relations_path: str) -> str:
        """
        Genera una consulta DAX basada en la pregunta del usuario y los archivos de contexto.
        Args:
            user_question: La pregunta del usuario en lenguaje natural.
            model_data_path: Ruta al archivo JSON del modelo de datos.
            relations_path: Ruta al archivo JSON de las relaciones.
        Returns:
            La consulta DAX generada por el modelo como una cadena de texto.
        """
        print("Cargando archivos de contexto...")
        model_data_content = self._load_json_as_string(model_data_path)
        relations_content = self._load_json_as_string(relations_path)

        print("Construyendo el prompt final...")
        system_prompt = self.SYSTEM_PROMPT_TEMPLATE.format(
            modelo_datos=model_data_content,
            relaciones=relations_content
        )

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_question),
        ]

        print(f"Enviando la pregunta al modelo: '{user_question}'")
        try:
            response = self.model.invoke(messages)
            return response.content
        except LangChainException as e:
            print(f"Ocurrió un error al invocar el modelo de IA: {e}")
            return "Error: No se pudo generar la consulta DAX."
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return "Error: Falla inesperada en el sistema."


def main():
    """
    Función principal para ejecutar el asistente DAX desde la línea de comandos.
    """
    # Configura el parser de argumentos para aceptar una pregunta desde la terminal
    parser = argparse.ArgumentParser(description="Asistente para generar consultas DAX usando IA.")
    parser.add_argument(
        "pregunta",
        type=str,
        nargs='?',
        default=None,  # No valor por defecto, así forzamos a pedirlo si no se pasa
        help="La pregunta en lenguaje natural para generar la consulta DAX."
    )
    parser.add_argument(
        "--modelo_datos",
        type=str,
        default="D:\\ai-dax\\modelo_datos.json",
        help="Ruta al archivo JSON del modelo de datos."
    )
    parser.add_argument(
        "--relaciones",
        type=str,
        default="D:\\ai-dax\\relaciones.json",
        help="Ruta al archivo JSON de las relaciones del modelo."
    )
    args = parser.parse_args()

    # Si no se pasó la pregunta como argumento, pedirla por consola
    if not args.pregunta:
        args.pregunta = input("Introduce la pregunta en lenguaje natural para generar la consulta DAX: ")

    try:
        # Instancia y ejecuta el asistente
        asistente = DAXAssistant()
        consulta_dax = asistente.generate_dax_query(
            user_question=args.pregunta,
            model_data_path=args.modelo_datos,
            relations_path=args.relaciones
        )
        
        # Imprime el resultado final
        print("\n" + "="*25 + " CONSULTA DAX GENERADA " + "="*25)
        print(consulta_dax)
        print("="*73 + "\n")

    except ValueError as e:
        print(f"\nError de configuración: {e}")
    except Exception as e:
        print(f"\nOcurrió un error crítico: {e}")

# Punto de entrada del script
if __name__ == "__main__":
    main()
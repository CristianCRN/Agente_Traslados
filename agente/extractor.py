from openai import OpenAI
import json
import os
from dotenv import load_dotenv


load_dotenv()
# ── API ──
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
CAMPOS_PRINCIPALES = {"descripcion", "proyecto"}

def traslados(text):
    prompt = f"""
    Eres un experto en llenado de traslados, debes de sacar en una estructura JSON los siguientes datos:
    {{
        "descripcion": "",  
        "proyecto": ""
    }}
    Tener en cuenta que debes registrar en la descripcion el traslado completo, cada vez que el usuario escriba traslado, en descripcion agregas el recorrido,
    ejemplo: traslado Confa a Oficina, escirbes en descripcion Confa a Oficina, y el proyecto lo da el usuario tambien, el valor es un dato estandar, pero nunca lo agreges en la columna de proyecto.
    Si el usuario no menciona el proyecto o no da un recorrido claro, deja ese campo como string vacío (""), NO inventes ni asumas un valor.
    Texto del usuario {text}
    """
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages= [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            ] }],
        response_format={"type": "json_object"},
        temperature=0
    )
    
    respuesta=response.choices[0].message.content
    #print ("Devolvio", respuesta)
    return  json.loads(respuesta)

def validacion_respuesta(datos):
    respuesta=datos
    for campo in CAMPOS_PRINCIPALES:
        if campo not in respuesta:
            raise ValueError(f"JSON incompleto, falta campo principal: {campo}")
    
    return respuesta


import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_URL")
def inicializar():
    #Conexion a la base de datos con with para que guarde y cierre directamente 
    with psycopg2.connect(DB_NAME) as conexion:
        cursor = conexion.cursor()
        #Crear Tabla en caso de que no exista
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Traslados (
                ID SERIAL PRIMARY KEY,
                DIA TEXT,
                MES TEXT, 
                
                ANO TEXT,
                DESCRIPCION TEXT,
                PROYECTO TEXT, 
                VALOR NUMERIC
            )
        """)
        print("Base de datos y tabla listas")

if __name__ == "__main__":
    inicializar()
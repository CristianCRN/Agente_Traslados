import psycopg2
from database.modelos import DB_NAME
import os
from dotenv import load_dotenv

load_dotenv()
valor = os.getenv("VALOR_TRASLADO")

def guardar_traslado(dia, mes, ano, descripcion, proyecto):
    try:
        with psycopg2.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO Traslados (dia, mes, ano, descripcion, proyecto, valor)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (dia, mes, ano, descripcion, proyecto, valor))
    except Exception as e:
        print (f"Error al guardar los gastos: {e}")               
def obtener_traslado():
    with psycopg2.connect(DB_NAME) as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Traslados")
        return cursor.fetchall()
           
def traslado_mes(mes, ano):
    with psycopg2.connect(DB_NAME) as conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM Traslados
            WHERE mes=%s AND ano=%s 
            ORDER BY dia DESC
        """, (mes, ano))
        return cursor.fetchall()

import sqlite3
import pathlib

DB_NAME = str(pathlib.Path(__file__).parent.parent / "Traslados.db")

def inicializar():
    #Conexion a la base de datos con with para que guarde y cierre directamente 
    with sqlite3.connect(DB_NAME) as conexion:
        cursor = conexion.cursor()
        #Crear Tabla en caso de que no exista
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Traslados (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DIA TEXT,
                MES TEXT, 
                ANO TEXT,
                DESCRIPCION TEXT,
                PROYECTO TEXT, 
                VALOR REAL
            )
        """)
        print("Base de datos y tabla listas")

if __name__ == "__main__":
    inicializar()
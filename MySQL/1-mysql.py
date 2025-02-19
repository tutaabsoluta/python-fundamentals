import mysql.connector
import os


CONFIG_DB = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def conectar():
    try:
        conexion = mysql.connector.connect(**CONFIG_DB)
        if conexion.is_connected():
            print('Conexion a MySQL exitosa')
            return  conexion
    except mysql.connector.Error as err:
        print(f'Error de conexion: {err}')
        return None

if __name__ == "__main__":
    conectar()
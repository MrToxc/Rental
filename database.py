import json
import os
import pyodbc

connection = None

def get_db_connection():
    global connection

    if connection:
        return connection
    config_path = 'config.json'
    if not os.path.exists(config_path):
        raise Exception("Soubor config.json neexistuje! Vytvořte ho podle config.example.json.")

    with open(config_path, 'r') as f:
        config = json.load(f)

    conn_str = (
        f"DRIVER={config['driver']};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        f"UID={config['uid']};"
        f"PWD={config['pwd']}"
    )

    connection = pyodbc.connect(conn_str)
    return connection

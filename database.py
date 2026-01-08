import json
import os
from dataclasses import asdict

import pyodbc

def get_db_connection():
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

    return pyodbc.connect(conn_str)

def insert(table, obj):
    record = asdict(obj)
    record.pop(f"id_{table}", None)

    with get_db_connection() as connection:
        cursor = connection.cursor()
        attributes = ", ".join(record.keys())
        question_marks = ", ".join(["?"] * len(record.keys()))

        sql = f"INSERT INTO {table} ({attributes}) OUTPUT INSERTED.id_{table} VALUES ({question_marks})"
        cursor.execute(sql, *record.values())

        id_record = cursor.fetchone()[0]
        connection.commit()
        return id_record

def delete(table, id_record):
    with get_db_connection() as connection:
        cursor = connection.cursor()
        sql = f"DELETE FROM {table} WHERE id_{table} = ?"
        cursor.execute(sql, id_record)
        connection.commit()
        return cursor.rowcount > 0


def update(TABLE_NAME, obj):
    return None
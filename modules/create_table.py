import sqlite3

def create_table(cursor, name_table):
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {name_table} (id INTEGER PRIMARY KEY)')
    
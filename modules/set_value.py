
def set_value(cursor: object, name_table: str, name_parameters: str, value_parameters: str):
    cursor.execute(f"INSERT INTO {name_table} {name_parameters} VALUES {value_parameters}")
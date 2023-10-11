#
def add_column(cursor: object, name_table: str, name_column: str, type_column: str):
    cursor.execute(f"ALTER TABLE {name_table} ADD COLUMN {name_column} {type_column}") 
    
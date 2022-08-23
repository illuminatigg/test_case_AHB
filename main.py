from commands_core import DBConnection, Copy

connect = DBConnection(db_name='', user_name='', password='', host='', port='')
sql_copy = Copy()


def import_csv_to_database(table_name: str, fields: list, file_path, delimiter: str):
    sql_copy.set_command(table_name, fields, file_path, delimiter)
    connect.connect_and_run(sql_copy.get_command())


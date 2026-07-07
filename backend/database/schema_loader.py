from sqlalchemy import inspect
from database.connection import engine


def get_schema():

    inspector = inspect(engine)

    result = []

    for table in inspector.get_table_names():

        columns = []

        for col in inspector.get_columns(table):

            columns.append({
                "name": col["name"],
                "type": str(col["type"])
            })

        result.append({
            "table": table,
            "columns": columns
        })

    return result
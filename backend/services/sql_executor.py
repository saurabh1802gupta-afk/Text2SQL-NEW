from sqlalchemy import text
from database.connection import engine


def execute_sql(query: str):

    try:
        # Allow only SELECT queries
        if not query.strip().upper().startswith("SELECT"):
            return {
                "error": "Only SELECT queries are allowed"
            }

        with engine.connect() as conn:

            result = conn.execute(text(query))

            rows = result.fetchall()

            columns = result.keys()

            return [
                dict(zip(columns, row))
                for row in rows
            ]

    except Exception as e:

        return {
            "error": str(e)
        }
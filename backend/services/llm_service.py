from ollama import chat
from config.settings import OLLAMA_MODEL


def generate_sql(
    question: str,
    schema: str
):

    response = chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "system",
                "content": """
                You are an expert PostgreSQL Text-to-SQL assistant.

                Rules:
                - Return ONLY SQL
                - No markdown
                - No explanations
                - Use PostgreSQL syntax
                - Generate ONLY SELECT statements
                - Never generate INSERT
                - Never generate UPDATE
                - Never generate DELETE
                - Never generate DROP
                - Never generate ALTER
                - Never generate TRUNCATE
                """
            },
            {
                "role": "user",
                "content": f"""
                    Database Schema:
                    {schema}

                    Question:
                    {question}
                """
            }
        ],
        options={
            "temperature": 0
        }
    )

    sql = response["message"]["content"].strip()

    # Remove markdown if model accidentally returns it
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    # Safety validation
    if not sql.upper().startswith("SELECT"):
        raise ValueError(
            f"Unsafe SQL generated: {sql}"
        )

    print("=" * 50)
    print("QUESTION:")
    print(question)
    print()
    print("GENERATED SQL:")
    print(sql)
    print("=" * 50)

    return sql
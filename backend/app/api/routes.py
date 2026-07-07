from fastapi import APIRouter
from services.llm_service import generate_sql
from database.schema_loader import load_schema

router = APIRouter()


@router.post("/query")
def text_to_sql(
    body: dict
):

    question = body["question"]

    schema = load_schema()

    sql = generate_sql(
        question,
        schema
    )

    return {
        "question": question,
        "generated_sql": sql
    }
from fastapi import FastAPI
from database.connection import engine
from database.schema_loader import get_schema
from services.llm_service import generate_sql
from services.sql_executor import execute_sql
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    question: str
    generated_sql: str
    data: list

@app.get("/health")
def health():

    try:
        with engine.connect():

            return {"status": "connected"}

    except Exception as e:

        return {"error": str(e)}


@app.get("/schema")
def schema():

    return get_schema()



@app.post(
    "/query",
    response_model=QueryResponse
)
def query(data: QueryRequest):

    try:
        question = data.question

        SCHEMA = get_schema()

        sql = generate_sql(
            question=question,
            schema=SCHEMA
        )
        sql_clean = sql.strip().upper()

        if not sql_clean.startswith("SELECT"):
            raise HTTPException(
                status_code=400,
                detail="Only SELECT queries are allowed"
            )
        result = execute_sql(sql)

        return {
            "question": question,
            "generated_sql": sql,
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    question: str = Field(min_length=3)

class Source(BaseModel):
    document: str
    score: float

class QueryResponse(BaseModel):
    answer: str
    sources: list[Source]
    route: str
    grounded: bool

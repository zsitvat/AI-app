from pydantic import BaseModel

from schemas.model_schema import ModelSchema


class Tool(BaseModel):
    name: str
    parameters: dict | None = None


class SearchKwargs(BaseModel):
    k: int
    threshold: float = 0.5
    search_type: str = "similarity"


class RetriverTool(Tool):
    vector_db_path: str
    required: bool = False
    model: ModelSchema
    search_kwargs: SearchKwargs = SearchKwargs(
        k=5, threshold=0.5, search_type="similarity"
    )


class WebSearchTool(Tool):
    engine: str = "google"

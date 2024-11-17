from pydantic import BaseModel

from schemas.model_schema import ModelSchema

class SearchKwargs(BaseModel):
    k: int
    threshold: float = 0.5
    search_type: str = "similarity"

class Tool(BaseModel):
    tool_name: str
    parameters: dict = None

class RetriverTool(Tool):
    vector_db_path: str
    model: ModelSchema
    search_kwargs: SearchKwargs = None

class WebSearchTool(Tool):
    pass




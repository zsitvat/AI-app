from pydantic import BaseModel

from utils.prompt_templates import default_prompt
from schemas.model_schema import ModelSchema


class RequestPostSchema(BaseModel):
    prompt: str = default_prompt
    userInput: str
    model: ModelSchema
    vector_db_paths: list = None
    document_paths: list = None

from pydantic import BaseModel

from schemas.model_schema import ModelSchema
from schemas.tool_schema import Tool


class RequestPostSchema(BaseModel):
    prompt: str
    userInput: str
    model: ModelSchema
    tools_to_use: list[Tool] = None

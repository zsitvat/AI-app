from pydantic import BaseModel
from uuid import UUID,uuid4

from schemas.model_schema import ModelSchema
from schemas.tool_schema import Tool,WebSearchTool,RetriverTool


class AnswerRequestPostSchema(BaseModel):
    prompt: str
    user_input: str
    model: ModelSchema
    tools: list[Tool|WebSearchTool|RetriverTool] = None
    session_id: UUID|str = uuid4()

from pydantic import BaseModel
from typing import Optional

from schemas.model_schema import ModelSchema
from schemas.tool_schema import Tool, WebSearchTool, RetriverTool


class AnswerRequestPostSchema(BaseModel):
    prompt: str
    user_input: str
    model: ModelSchema
    tools: Optional[list[Tool | WebSearchTool | RetriverTool]]

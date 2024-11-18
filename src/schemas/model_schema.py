from pydantic import BaseModel
from enum import Enum


class ModelProviderType(str, Enum):
    OPENAI = "openai"
    AZURE = "azure"
    ANTHROPIC = "anthropic"
    BEDROCK = "bedrock"


class ModelType(str, Enum):
    EMBEDDING = "embedding"
    CHAT = "chat"
    COMPLETIONS = "completions"


class ModelSchema(BaseModel):
    model_name: str = "gpt-4o-mini"
    model_type: ModelType = ModelType.CHAT
    deployment: str | None = None
    provider: ModelProviderType = ModelProviderType.OPENAI
    temperature: int = 0

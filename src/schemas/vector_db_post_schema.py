from pydantic import BaseModel
from enum import Enum

from schemas.model_schema import ModelSchema

class VectorDbPostSchema(BaseModel):
    db_name: str = "deeplake_db"
    db_path: str = ""
    db_type: str = "deeplake"
    file_load_encoding = "utf-8"
    documents: list
    chunk_size: int = 2000
    chunk_overlap: int = 100
    overwrite: bool = False
    model: ModelSchema

class ModelProviderType(str, Enum):
    OPENAI = "openai"
    AZURE = "azure"

class EmbeddingModelSchema(BaseModel):
    model_name: str = "text-embedding-3-large"
    provider: ModelProviderType = ModelProviderType.OPENAI

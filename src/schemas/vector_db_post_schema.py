from pydantic import BaseModel
from enum import Enum

from schemas.model_schema import ModelSchema

class VectorDbPostSchema(BaseModel):
    db_path: str = "./vector_db"
    db_type: str = "deeplake"
    file_load_encoding: str = "utf-8"
    documents: list
    chunk_size: int = 2000
    chunk_overlap: int = 100
    overwrite: bool = False
    model: ModelSchema
    sheet_name: str = None

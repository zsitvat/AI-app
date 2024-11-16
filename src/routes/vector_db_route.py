from fastapi import APIRouter, Response
import logging

from services.vector_db.vector_db import VectorDb
from schemas.vector_db_post_schema import VectorDbPostSchema

router = APIRouter()

@router.post('/api/vector_db/create')
def rag(request: VectorDbPostSchema):
    """ Create a vector database route"""
    
    if request != None:
        try:

            return VectorDb().create_vector_db_deeplake(
            path=request.db_path+request.db_name,
            chunk_size=request.chunk_size,
            chunk_overlap=request.chunk_overlap,
            overwrite=request.overwrite,
            documents=request.documents,
            model=request.model,
            encoding = request.file_load_encoding
            )

        except Exception as ex:
            logging.error(f"Error in question answer route: {str(ex)}")
            return Response(content="Error in question answer route", status_code=500, media_type="application/json")
    else:
        return Response(content="No parameters found!", status_code=400, media_type="application/json")

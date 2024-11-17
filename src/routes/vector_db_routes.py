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

            if request.db_type == "deeplake":
                return VectorDb().create_vector_db_deeplake(
                    db_path=request.db_path,
                    chunk_size=request.chunk_size,
                    chunk_overlap=request.chunk_overlap,
                    overwrite=request.overwrite,
                    documents=request.documents,
                    model=request.model,
                    encoding = request.file_load_encoding,
                    sheet_name = request.sheet_name
                )
            else:
                raise Exception("Vector database type is not supported!")  
                   

        except Exception as ex:
            logging.error(f"Error in vector_db/create route: {str(ex)}")
            return Response(content="Error in vector_db/create route", status_code=500, media_type="application/json")
    else:
        return Response(content="No parameters found!", status_code=400, media_type="application/json")

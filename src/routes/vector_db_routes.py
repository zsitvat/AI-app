from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import logging

from services.vector_db.vector_db import VectorDb
from schemas.vector_db_post_schema import VectorDbPostSchema

router = APIRouter()


@router.post("/api/vector_db/create")
def rag(request: VectorDbPostSchema):
    """Create a vector database route"""

    try:

        if request.db_type == "deeplake":
            return VectorDb().create_vector_db_deeplake(
                db_path=request.db_path,
                chunk_size=request.chunk_size,
                chunk_overlap=request.chunk_overlap,
                overwrite=request.overwrite,
                documents=request.documents,
                model=request.model,
                encoding=request.file_load_encoding,
                sheet_name=request.sheet_name,
            )
        else:
            raise HTTPException(
                status_code=400, detail="Vector database type is not supported!"
            )

    except Exception as ex:
        logging.getLogger("logger").error(f"Error in vector_db/create route: {str(ex)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing the request in vector_db/create: {str(ex)}",
        )

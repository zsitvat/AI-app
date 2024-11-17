from fastapi import APIRouter, Response
import logging

from services.question_answer.question_answer_service import QuestionAnswerService
from schemas.request_post_schema import RequestPostSchema

router = APIRouter()


@router.post("/api/question_answer")
def question_answer(request_data: RequestPostSchema):

    if request_data != None:
        try:

            answer_service = QuestionAnswerService(
                prompt=request_data.prompt,
                model=request_data.model,
                vector_db_paths=request_data.vector_db_paths,
                document_paths=request_data.document_paths,
            )
            return answer_service.run_agent(request_data.userInput)

        except Exception as ex:
            logging.error(f"Error in question_answer route: {str(ex)}")
            return Response(
                content="Error in rag route",
                status_code=500,
                media_type="application/json",
            )
    else:
        return Response(
            content="No parameters found!",
            status_code=400,
            media_type="application/json",
        )
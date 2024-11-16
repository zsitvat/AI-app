from fastapi import APIRouter, Response
import logging

from services.question_answer.question_answer_service import QuestionAnswerService
from schemas.request_post_schema import RequestPostSchema

router = APIRouter()

@router.post('/api/question_answer')
def rag(request_data: RequestPostSchema):
    
    if request_data != None and request_data.parameters != None:
        try:
            params = {
               
            }

            answer_service = QuestionAnswerService(params)
            return answer_service.create_response(request_data.userInput)

        except Exception as ex:
            logging.error(f"Error in rag route: {str(ex)}")
            return Response(content="Error in rag route", status_code=500, media_type="application/json")
    else:
        return Response(content="No parameters found!", status_code=400, media_type="application/json")

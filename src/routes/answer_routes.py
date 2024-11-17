from fastapi import APIRouter, Response
import logging


from schemas.answer_post_schema import AnswerRequestPostSchema
from services.answer.answer_service import AnswerService

router = APIRouter()


@router.post("/api/answer")
def question_answer(request_data: AnswerRequestPostSchema):

    if request_data != None:
        try:

            answer_service = AnswerService(
                prompt=request_data.prompt,
                model=request_data.model,
                tools_config = request_data.tools,
                session_id = request_data.session_id
            )
            return answer_service.run_agent(request_data.user_input)

        except Exception as ex:
            logging.getLogger("logger").error(f"Error in answer route: {str(ex)}")
            return Response(
                content=f"Error in answer route  {str(ex)}",
                status_code=500,
                media_type="application/json",
            )
    else:
        return Response(
            content="No parameters found!",
            status_code=400,
            media_type="application/json",
        )
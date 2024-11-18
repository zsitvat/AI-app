from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import logging


from schemas.answer_post_schema import AnswerRequestPostSchema
from services.answer.answer_service import AnswerService

router = APIRouter()


@router.post("/api/answer")
def question_answer(request_data: AnswerRequestPostSchema):

    try:

        answer_service = AnswerService(
            prompt=request_data.prompt,
            model=request_data.model,
            tools_config=request_data.tools,
            session_id=request_data.session_id,
        )
        result = answer_service.run_agent(request_data.user_input)
        return JSONResponse(content={"answer": result}, status_code=200)

    except Exception as ex:
        logging.getLogger("logger").error(f"Error in answer route: {str(ex)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing the request in answer route: {str(ex)}",
        )

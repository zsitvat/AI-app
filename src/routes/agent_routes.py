from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import logging


from schemas.agent_request_post_schema import AgentRequestPostSchema
from services.agent.agent_service import AgentService

router = APIRouter()


@router.post("/api/agent/answer")
def agent_answer(request_data: AgentRequestPostSchema):

    try:

        answer_service = AgentService(
            prompt=request_data.prompt,
            model=request_data.model,
            tools_config=request_data.tools,
            user_id = request_data.user_id
        )

        result = answer_service.get_agent_answer(user_input=request_data.user_input)

        return JSONResponse(content={"answer": result}, status_code=200)

    except Exception as ex:
        logging.getLogger("logger").error(f"Error in agent answer route: {str(ex)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing the request in agent answer route: {str(ex)}",
        )

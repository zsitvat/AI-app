from pydantic import BaseModel


from utils.prompt_templates import default_prompt

class RequestPostSchema(BaseModel):
    prompt : str = default_prompt
    userInput : str
    documents : list = None

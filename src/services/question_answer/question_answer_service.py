

from utils.model_selector import get_model
from schemas.model_schema import ModelSchema
from langchain import hub

class QuestionAnswerService:
    def __init__(self, prompt:str, model:ModelSchema, vector_db_paths:list, document_paths:list):
        self.prompt = prompt
        self.model = model
        self.vector_db_paths = vector_db_paths
        self.document_paths = document_paths
        self.chat_model = get_model

    def run_agent(self, userInput):
        
        model = get_model(
            model = self.model.model_name,
            deployment=self.model.deployment,
            provider=self.model.provider,
            type=self.model.model_type,
            temperature=self.model.temperature
            )
        
        prompt = hub.pull(self.prompt)
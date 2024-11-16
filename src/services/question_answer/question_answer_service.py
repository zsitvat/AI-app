from utils.model_selector import get_model

class QuestionAnswerService:
    def __init__(self, prompt, model, vector_db_paths, document_paths):
        self.prompt = prompt
        self.model = model
        self.vector_db_paths = vector_db_paths
        self.document_paths = document_paths
        self.chat_model = get_model

        
    

    def answer_from_document(self, userInput):
        
       pass

    def run_agent(self, userInput):
        pass
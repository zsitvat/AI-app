from langchain_core.tools import tool
from langchain_community.vectorstores.deeplake import DeepLake

from utils.model_selector import get_model
from schemas.request_post_schema import Tool



@tool
def retriver_tool(parameters:dict, user_input:str) -> list:
    """ This tool is used to retrive the documents from the document database
    Args:
        user_input (str): The user input to be used to retrive the documents
    Returns:
        list: The list of documents retrived from the document database
    """

    
    embedding = get_model(
        provider=parameters.model.provider,
        deployment=parameters.model.deployment,
        model=parameters.model.model_name,
        type=parameters.model.model_type,
        temperature=parameters.model.temperature,
    )

    retriver = DeepLake(
        embedding=embedding,
        dataset_path=parameters.vector_db_path
    ).as_retriever(
        search_type=parameters.search_kwargs.search_type,
        k=parameters.search_kwargs.k, 
        threshold=parameters.search_kwargs.threshold
    )

    return retriver.invoke(user_input)
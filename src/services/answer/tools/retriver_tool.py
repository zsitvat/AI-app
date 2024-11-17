from langchain_core.tools import tool
from langchain_community.vectorstores.deeplake import DeepLake

from utils.model_selector import get_model
from schemas.model_schema import ModelSchema
from schemas.tool_schema import RetriverTool
from langchain.embeddings.base import Embeddings


@tool
def retriver_tool(tool_config: RetriverTool, user_input: str) -> list:
    """
    Web search tool used to search the web for information.

    Args:
        tool_config (dict): The parameters used for the retrieval.
        user_input (str): The user input used to retrieve the information.

    Returns:
        list: A list of documents retrieved from the web.

    """

    model = tool_config.model

    embedding = get_model(
        provider=model.provider,
        deployment=model.deployment,
        type=model.model_type,
        model=model.model_name,
    )

    if not isinstance(embedding, Embeddings):
        raise TypeError("Expected an instance of Embeddings")

    retriver = DeepLake(
        embedding=embedding, dataset_path=tool_config.vector_db_path, read_only=True
    ).as_retriever(
        search_type=tool_config.search_kwargs.search_type,
        k=tool_config.search_kwargs.k,
        threshold=tool_config.search_kwargs.threshold,
    )

    return retriver.invoke(user_input)

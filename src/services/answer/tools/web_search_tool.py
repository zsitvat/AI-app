from langchain_core.tools import tool
from langchain_community.utilities import SerpAPIWrapper
import logging

from schemas.tool_schema import WebSearchTool


@tool
def web_search_tool(tool_config: WebSearchTool, user_input: str) -> list|str:
    """
    Web search tool is used to search the web for information

    Args:
        tool_config (dict): The parameters to be used for the retrival
        user_input (str): The user input to be used to retrive the documents

    Returns:
        list: The list of documents retrived from the document database
    """

    try:

        search = SerpAPIWrapper(params={"engine": tool_config.engine})

        search_results = search.run(user_input)

        return search_results

    except Exception as ex:
        logging.getLogger("logger").error(f"Error in web_search_tool: {e}")
        raise Exception(f"Error in web_search_tool: {e}")
    
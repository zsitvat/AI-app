from langchain import hub
from langchain_core.language_models.base import BaseLanguageModel

import logging

from utils.model_selector import get_model
from schemas.model_schema import ModelSchema
from schemas.tool_schema import Tool
from .tools_config import AVAILABLE_TOOLS


class AnswerService:
    """Service to get answer from the model and tools"""

    def __init__(self, prompt: str, model: ModelSchema, tools_config: list[Tool]):
        self.prompt = prompt
        self.model = model
        self.tools_config = tools_config

    def get_ai_answer(self, user_input: str) -> str:
        """Run the chain to get answer the user input based on the model and tools

        Args:
            user_input (str): User input

        Returns:
            str: Answer from the model
        """
        logging.getLogger("logger").debug("Starting to get AI answer")

        model_tools = []

        try:

            for tool in self.tools_config:
                if tool.name in AVAILABLE_TOOLS:
                    model_tools.append(AVAILABLE_TOOLS[tool.name])
                else:
                    logging.getLogger("logger").warning(
                        f"Tool {tool.name} not found in available tools"
                    )

            llm = get_model(
                model=self.model.model_name,
                deployment=self.model.deployment,
                provider=self.model.provider,
                type=self.model.model_type,
                temperature=self.model.temperature,
            )

            if not isinstance(llm, BaseLanguageModel):
                logging.getLogger("logger").error(
                    "The model returned by get_model is not an instance of BaseLanguageModel"
                )
                raise TypeError(
                    "The model returned by get_model is not an instance of BaseLanguageModel"
                )

            llm_with_tools = llm.bind_tools(model_tools, tool_choice="auto")

            prompt = hub.pull(self.prompt)

            chain = prompt | llm_with_tools

            if any(
                tool.name == "retriver_tool" and tool.required == True
                for tool in self.tools_config
            ):
                documents = AVAILABLE_TOOLS["retriver_tool"].invoke(
                    {
                        "tool_config": next(
                            config
                            for config in self.tools_config
                            if config.name == "retriver_tool"
                        ),
                        "user_input": user_input,
                    }
                )

            result = chain.invoke(
                {
                    "question": user_input,
                    "documents": [doc.page_content for doc in documents],
                }
            )

            if result.tool_calls:
                docs = []
                for tool_call in result.tool_calls:
                    tool_config = next(
                        config
                        for config in self.tools_config
                        if config.name == tool_call["name"]
                    )
                    tool_result = AVAILABLE_TOOLS[tool_call["name"]].invoke(
                        {"tool_config": tool_config, **tool_call["args"]}
                    )

                    docs.append(tool_result)

                result = chain.invoke({"question": user_input, "documents": docs})

            logging.getLogger("logger").debug(f"AI answer received {result.content}")

            return result.content

        except Exception as ex:
            logging.getLogger("logger").error(f"Error while getting AI answer: {ex}")
            raise ex

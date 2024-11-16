from langchain_community.llms.openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_community.chat_models import AzureChatOpenAI
from langchain_openai import OpenAI, AzureOpenAI, ChatOpenAI, AzureChatOpenAI, OpenAIEmbeddings, AzureOpenAIEmbeddings
from langchain_core.language_models.base import BaseLanguageModel
from langchain_anthropic import ChatAnthropic
from langchain_aws import ChatBedrock

import os
import logging
import boto3


def get_model(
    provider: str,
    deployment: str | None = None,
    model: str | None = 'gtp-3.5-turbo',
    type: str = "general",
    temperature: float = 0
) -> (BaseLanguageModel):

    if type == "general":
        if provider == "openai":
            return OpenAI(model=model, temperature=temperature)
        elif provider == "azure":
            return AzureOpenAI(
                azure_endpoint=os.environ.get('AZURE_BASE_URL'),
                openai_api_version=os.environ.get('AZURE_API_VERSION'),
                azure_deployment=deployment,
                temperature=temperature
            )
    if type == "chat":
        if provider == "openai":
            return ChatOpenAI(model=model, temperature=temperature)
        elif provider == "azure":
            return AzureChatOpenAI(
                azure_endpoint=os.environ.get('AZURE_BASE_URL'),
                openai_api_version=os.environ.get('AZURE_API_VERSION'),
                azure_deployment=deployment,
                temperature=temperature
            )
        elif provider == "anthropic":
            return ChatAnthropic(
                model=model,
                temperature=temperature
            )
        elif provider == "bedrock":
            client = boto3.client(
                    service_name="bedrock-runtime",
                    region_name=os.environ.get('BEDROCK_AWS_REGION_NAME'),
                    aws_access_key_id=os.environ.get('BEDROCK_AWS_ACCESS_KEY'),
                    aws_secret_access_key=os.environ.get('BEDROCK_AWS_SECRET_KEY')
                )
                
            return ChatBedrock(
                client=client,
                model_id=model,
                model_kwargs=dict(temperature=temperature)
            )
        else:
            logging.getLogger("uvicorn").error("Wrong model provider!")
            raise KeyError("wrong model provider")
    elif type == "embedding":
        if provider == "openai":
            return OpenAIEmbeddings(model=model)
        elif provider == "azure":
            return AzureOpenAIEmbeddings(
                azure_endpoint=os.environ.get('AZURE_BASE_URL'),
                openai_api_version=os.environ.get('AZURE_API_VERSION'),
                azure_deployment=deployment
            )
        else:
            logging.getLogger("uvicorn").error("Wrong model provider!")
            raise KeyError("wrong model provider")
    else:
        logging.getLogger("uvicorn").error("Wrong model type!")
        raise KeyError("wrong model type")

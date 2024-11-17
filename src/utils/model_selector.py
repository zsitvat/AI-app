from langchain_community.llms.openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_community.chat_models import AzureChatOpenAI
from langchain_openai import OpenAI, AzureOpenAI, ChatOpenAI, AzureChatOpenAI, OpenAIEmbeddings, AzureOpenAIEmbeddings
from langchain_core.language_models.base import BaseLanguageModel
from langchain_core.embeddings import Embeddings
from langchain_anthropic import ChatAnthropic
from langchain_aws import ChatBedrock

import os
import logging
import boto3


def get_model(
    provider: str,
    deployment: str | None = None,
    model: str = 'gpt-4o-mini',
    type: str = "completions",
    temperature: float = 0
):

    if type == "completions":
        if provider == "openai":
            if model is None:
                raise ValueError("Model cannot be None")
            return OpenAI(model=model, temperature=temperature)
        elif provider == "azure":
            return AzureOpenAI(
                azure_endpoint=os.environ.get('AZURE_BASE_URL'),
                azure_deployment=deployment,
                temperature=temperature
            )
    if type == "chat":
        if provider == "openai":
            return ChatOpenAI(model=model, temperature=temperature)
        elif provider == "azure":
            return AzureChatOpenAI(
                azure_endpoint=os.environ.get('AZURE_BASE_URL'),
                azure_deployment=deployment,
                temperature=temperature
            )
        elif provider == "anthropic":
            return ChatAnthropic(
                model_name=model,
                temperature=temperature,
                timeout=60,
                stop=None
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
                model=model,
                model_kwargs=dict(temperature=temperature)
            )
        else:
            logging.getLogger("logger").error("Wrong model provider!")
            raise KeyError("wrong model provider")
    elif type == "embedding":
        if provider == "openai":
            return OpenAIEmbeddings(model=model)
        elif provider == "azure":
            return AzureOpenAIEmbeddings(
                azure_endpoint=os.environ.get('AZURE_BASE_URL'),
                azure_deployment=deployment
            )
        else:
            logging.getLogger("logger").error("Wrong model provider!")
            raise KeyError("wrong model provider")
    else:
        logging.getLogger("logger").error("Wrong model type!")
        raise KeyError("wrong model type")

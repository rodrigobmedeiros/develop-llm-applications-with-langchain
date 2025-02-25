from typing import Type
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import AzureChatOpenAI

from ice_breaker.env_config import EnvConfig
from ice_breaker.llm.azure_openai_config import default_token_provider


class LLMFactory:
    @staticmethod
    def create_llm(
        llm_type: str, env_config: Type[EnvConfig] = EnvConfig
    ) -> BaseChatModel:
        if llm_type == "Azure Open AI":
            return AzureChatOpenAI(
                temperature=0,
                api_version=env_config.AZURE_API_VERSION,
                model_name=env_config.AZURE_MODEL_NAME,
                azure_endpoint=env_config.AZURE_OPENAI_ENDPOINT,
                azure_ad_token_provider=default_token_provider,
            )
        else:
            raise ValueError("Invalid LLM type")

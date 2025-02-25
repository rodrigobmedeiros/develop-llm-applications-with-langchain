from azure.identity import ClientSecretCredential
from env_config import EnvConfig
from typing import Type

class AzureClientCredential:
    @staticmethod
    def get_credential(env_config: Type[EnvConfig] = EnvConfig) -> ClientSecretCredential:
        return ClientSecretCredential(
            tenant_id=env_config.AZURE_TENANT_ID,
            client_id=env_config.AZURE_CLIENT_ID,
            client_secret=env_config.AZURE_CLIENT_SECRET,
        )


def default_token_provider(
    credential: type[AzureClientCredential] = AzureClientCredential, env_config: Type[EnvConfig] = EnvConfig
) -> str:
    return credential.get_credential(env_config).get_token(env_config.AZURE_URL_TOKEN).token
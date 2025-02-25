from azure.identity import ClientSecretCredential
from env_config import EnvConfig
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from typing import Type

information = """
Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman known for his key roles in Tesla, Inc., SpaceX, and X, formerly Twitter (which he has owned since 2022). Since 2025, he has been a senior advisor to President Donald Trump and head of the Department of Government Efficiency (DOGE). Musk is the wealthiest person in the world; as of February 2025, Forbes estimates his net worth to be US$384 billion.

Musk was born to an affluent South African family in Pretoria before immigrating to Canada, acquiring Canadian citizenship via his mother. He moved to California in 1995 to attend Stanford University, and with his brother Kimbal co-founded the software company Zip2, which was acquired by Compaq in 1999. That same year, Musk co-founded X.com, a direct bank, that later formed PayPal. In 2002, Musk acquired U.S. citizenship, and eBay acquired PayPal. Using the money he made from the sale, Musk founded SpaceX, a spaceflight services company, in 2002. In 2004, Musk was an early investor in electric vehicle manufacturer Tesla and became its chairman and later CEO. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk for fraud, alleging he falsely announced that he had secured funding for a private takeover of Tesla; he stepped down as chairman and paid a fine. Musk was named Time magazine's Person of the Year in 2021. In 2022, he acquired Twitter, and rebranded the service as X the following year. In January 2025, he was appointed head of Trump's newly created DOGE.
"""

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

if __name__ == "__main__":
    print("Hello LangChain!")

    # Basically is a parametarized string used to standardize LLM prompts.
    summary_template: str = """
    Given the information {information} about a person I want to create:
    1. A short summary
    2. Two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", client=client)
    llm = AzureChatOpenAI(
        temperature=0,
        api_version=EnvConfig.AZURE_API_VERSION,
        model_name=EnvConfig.AZURE_MODEL_NAME,
        azure_endpoint=EnvConfig.AZURE_OPENAI_ENDPOINT,
        azure_ad_token_provider=default_token_provider
    )
    chain = summary_prompt_template | llm | StrOutputParser()
    response = chain.invoke(input={"information": information})

    print("================ Complete Response ================")
    print(response)

    print("================ Streamed Response ================")
    for idx, chunk in enumerate(chain.stream(input={"information": information})):
        print(f"Chunk {idx}: {chunk}")



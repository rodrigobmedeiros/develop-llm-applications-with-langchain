
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSerializable
from ice_breaker.llm.llm_factory import LLMFactory
from ice_breaker.third_parties.linkedin import scrape_linkedin_profile


information = """
Elon Reeve Musk (/ˈiːlɒn mʌsk/; born June 28, 1971) is a businessman known for his key roles in Tesla, Inc., SpaceX, and X, formerly Twitter (which he has owned since 2022). Since 2025, he has been a senior advisor to President Donald Trump and head of the Department of Government Efficiency (DOGE). Musk is the wealthiest person in the world; as of February 2025, Forbes estimates his net worth to be US$384 billion.

Musk was born to an affluent South African family in Pretoria before immigrating to Canada, acquiring Canadian citizenship via his mother. He moved to California in 1995 to attend Stanford University, and with his brother Kimbal co-founded the software company Zip2, which was acquired by Compaq in 1999. That same year, Musk co-founded X.com, a direct bank, that later formed PayPal. In 2002, Musk acquired U.S. citizenship, and eBay acquired PayPal. Using the money he made from the sale, Musk founded SpaceX, a spaceflight services company, in 2002. In 2004, Musk was an early investor in electric vehicle manufacturer Tesla and became its chairman and later CEO. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk for fraud, alleging he falsely announced that he had secured funding for a private takeover of Tesla; he stepped down as chairman and paid a fine. Musk was named Time magazine's Person of the Year in 2021. In 2022, he acquired Twitter, and rebranded the service as X the following year. In January 2025, he was appointed head of Trump's newly created DOGE.
"""



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
    llm = LLMFactory.create_llm(llm_type="Azure Open AI")
    chain: RunnableSerializable = summary_prompt_template | llm | StrOutputParser()
    information = scrape_linkedin_profile("https://www.linkedin.com/in/elonmusk/")
    response = chain.invoke(input={"information": information})

    print("================ Complete Response ================")
    print(response)

    print("================ Streamed Response ================")
    for idx, chunk in enumerate(chain.stream(input={"information": information})):
        print(f"Chunk {idx}: {chunk}")



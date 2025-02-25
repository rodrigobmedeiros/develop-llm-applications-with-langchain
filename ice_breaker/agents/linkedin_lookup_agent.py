from langchain_core.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from typing import Type
from ice_breaker.llm.llm_factory import LLMFactory
from ice_breaker.tools.tools import get_profile_url_tavily
from langchain_core.language_models.chat_models import BaseChatModel


def blabla(x: str) -> str:
    return "blablabla"


def lookup(name: str, llm_factory: Type[LLMFactory] = LLMFactory) -> str:
    # llm from factory
    llm: BaseChatModel = llm_factory.create_llm("Azure Open AI")
    # In our case this guy here would be the system prompt.
    template: str = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
        Your answer should contain only a URL"""
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the linkedin Page URL",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    response = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linkedin_profile_url: str = response.get("output")
    return linkedin_profile_url

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from typing import Any, Type

from ice_breaker.env_config import EnvConfig


def get_profile_url_tavily(name: str, env_config: Type[EnvConfig] = EnvConfig) -> Any:
    """Searches for Linkedin or Twitter Profile Page."""
    tavily_api_wrapper = TavilySearchAPIWrapper(
        tavily_api_key=env_config.TAVILY_API_KEY
    )
    search = TavilySearchResults(api_wrapper=tavily_api_wrapper)
    res = search.run(f"{name}")
    return res

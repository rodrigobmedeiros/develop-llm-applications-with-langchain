from ice_breaker.env_config import EnvConfig
import json
from pathlib import Path

MOCK_LINKEDIN_PROFILE = Path(__file__).parent / "mock" / "linkedin.json"

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool=False):
    """
    scrape information from linkedin profiles.
    Manually scrape the information from the linkedin profile"""
    with open(MOCK_LINKEDIN_PROFILE, "r") as f:
        return json.load(f)

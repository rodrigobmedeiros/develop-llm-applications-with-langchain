import json
from pathlib import Path

MOCK_LINKEDIN_PROFILE = Path(__file__).parent / "mock" / "linkedin.json"

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool=False):
    """
    scrape information from linkedin profiles.
    Manually scrape the information from the linkedin profile"""
    with open(MOCK_LINKEDIN_PROFILE, "r") as f:
        data = json.load(f).get("person")
        return {
            k: v 
            for k, v in data.items()
            if v not in [[], "", " ", None] and k not in ["certifications"]
        }
    



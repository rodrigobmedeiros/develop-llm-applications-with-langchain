from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Any

class Summary(BaseModel):
    summary: str = Field(..., description="summary")
    facts: list[str] = Field(..., description="interestinf facts about them")

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump()
    

summary_parser = PydanticOutputParser(pydantic_object=Summary)

from pydantic import BaseModel
from typing import Optional


class ProblemRequest(BaseModel):

    input_type: str
    content: str


class SolutionResponse(BaseModel):

    parsed_problem: Optional[str]
    answer: Optional[str]
    explanation: Optional[str]
    confidence: Optional[float]
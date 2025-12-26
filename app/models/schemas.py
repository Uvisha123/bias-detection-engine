from pydantic import BaseModel
from typing import Any, List

class BiasRequest(BaseModel):
    sensitive_attribute: str
    decision_column: str
    positive_decision_value: Any

class GroupResult(BaseModel):
    group: str
    total: int
    positive: int
    outcome_rate: float

class BiasResponse(BaseModel):
    bias_detected: bool
    disparate_impact_ratio: float
    results: List[GroupResult]

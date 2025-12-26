from fastapi import APIRouter
import pandas as pd

from app.models.schemas import BiasRequest, BiasResponse
from app.core.bias_engine import detect_outcome_bias

router = APIRouter()

@router.post("/analyze-bias", response_model=BiasResponse)
def analyze_bias(request: BiasRequest):
    df = pd.read_csv("data/sample.csv")
    data = df.to_dict(orient="records")

    return detect_outcome_bias(
        data=data,
        sensitive_attribute=request.sensitive_attribute,
        decision_column=request.decision_column,
        positive_value=request.positive_decision_value
    )

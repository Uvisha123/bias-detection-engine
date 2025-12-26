from typing import List, Dict, Any

def detect_outcome_bias(
    data: List[Dict[str, Any]],
    sensitive_attribute: str,
    decision_column: str,
    positive_value: Any) -> Dict[str, Any]:
    groups = {}

    for row in data:
        group = row[sensitive_attribute]
        decision = row[decision_column]

        if group not in groups:
            groups[group] = {"total": 0, "positive": 0}

        groups[group]["total"] += 1
        if decision == positive_value:
            groups[group]["positive"] += 1

    results = []
    rates = []

    for group, counts in groups.items():
        rate = counts["positive"] / counts["total"]
        rates.append(rate)

        results.append({
            "group": group,
            "total": counts["total"],
            "positive": counts["positive"],
            "outcome_rate": round(rate, 3)
        })

    min_rate = min(rates)
    max_rate = max(rates)

    ratio = round(min_rate / max_rate, 3)

    return {
        "results": results,
        "disparate_impact_ratio": ratio,
        "bias_detected": ratio < 0.8
    }

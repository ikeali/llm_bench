from sqlalchemy.orm import Session
from .models import SimulationResult

def rank_llms(metric_id: int, db: Session):
    """Ranks LLMs based on the simulation results for a given metric."""
    
    results = (
        db.query(SimulationResult)
        .filter(SimulationResult.metric_id == metric_id)
        .all()
    )

    if not results:
        return []

    llm_scores = {}
    for result in results:
        if result.llm_id not in llm_scores:
            llm_scores[result.llm_id] = []
        llm_scores[result.llm_id].append(result.value)

    rankings = []
    for llm_id, values in llm_scores.items():
        mean_value = sum(values) / len(values)
        rankings.append({"llm_id": llm_id, "mean_value": mean_value})

    # Sort by mean value (ascending order)
    rankings.sort(key=lambda x: x["mean_value"])
    
    return rankings

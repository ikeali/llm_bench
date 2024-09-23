from sqlalchemy.orm import Session
from sqlalchemy import func
from .models import SimulationResult, LLM

def rank_llms(metric_id: int, db: Session):
    """
    Ranks LLMs based on the simulation results for a given metric.
    This version uses database-side aggregation to calculate the mean.
    """
    try:
        # Perform a database query to calculate the mean value for each LLM
        rankings = (
            db.query(
                SimulationResult.llm_id,
                func.avg(SimulationResult.value).label('mean_value'),
                LLM.name
            )
            .join(LLM, LLM.id == SimulationResult.llm_id)  # Join with LLM table for LLM names
            .filter(SimulationResult.metric_id == metric_id)
            .group_by(SimulationResult.llm_id, LLM.name)
            .order_by(func.avg(SimulationResult.value))  # Order by the mean value (ascending)
            .all()
        )

        # If no results found, return an empty list
        if not rankings:
            return []

        ranked_llms = [
            {"llm_id": llm_id, "llm_name": llm_name, "mean_value": mean_value}
            for llm_id, mean_value, llm_name in rankings
        ]

        return ranked_llms

    except Exception as e:
        print(f"Error ranking LLMs: {e}")
        return []

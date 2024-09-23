import random
from sqlalchemy.orm import Session
from .models import LLM, Metric, SimulationResult
from .database import get_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_simulation_data(db: Session, num_points=1000, seed=None):
    if seed is not None:
        random.seed(seed)
    
    llms = db.query(LLM).all()
    metrics = db.query(Metric).all()
    
    try:
        for _ in range(num_points):
            for llm in llms:
                for metric in metrics:
                    value = random.uniform(0, 100)
                    simulation_result = SimulationResult(llm_id=llm.id, metric_id=metric.id, value=value)
                    db.add(simulation_result)
        db.commit()
        logger.info("Simulation data generated.")
    except Exception as e:
        logger.error("Error while generating simulation data: %s", str(e))
        db.rollback()


if __name__ == "__main__":
    db = next(get_db())
    generate_simulation_data(db)

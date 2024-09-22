import random
from sqlalchemy.orm import Session
from .models import LLM, Metric, SimulationResult
from .database import get_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_database(db: Session):
    logger.info("Seeding database with LLMs and metrics...")
    
    llms = [
        LLM(name='GPT-4o', description='Generative Pre-trained Transformer 4 OpenAI'),
        LLM(name='Llama 3.1 405', description='LLaMA model 3.1 405 billion parameters'),
        LLM(name='Mistral Large2', description='Mistral model Large 2'),
        LLM(name='Claude 3.5 Sonnet', description='Claude model 3.5 Sonnet'),
        LLM(name='Gemini 1.5 Pro', description='Gemini model 1.5 Pro'),
    ]

    try:
        for llm in llms:
            if not db.query(LLM).filter_by(name=llm.name).first():
                db.add(llm)

        metrics = [
            Metric(name='Time to First Token (TTFT)'),
            Metric(name='Tokens Per Second (TPS)'),
            Metric(name='End-to-End Request Latency (e2e_latency)'),
            Metric(name='Requests Per Second (RPS)'),
        ]

        for metric in metrics:
            if not db.query(Metric).filter_by(name=metric.name).first():
                db.add(metric)

        db.commit()
        logger.info("Database seeded successfully.")

    except Exception as e:
        logger.error("Error while seeding database: %s", str(e))
        db.rollback()


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
    seed_database(db)
    generate_simulation_data(db)

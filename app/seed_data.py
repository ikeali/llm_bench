import random
from datetime import datetime
from sqlalchemy.orm import Session
from .models import LLM, Metric
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

        # Bulk insert metrics
        metrics = []
        for i in range(100):
            metrics.append(Metric(
                name=f"Metric {i}",
                score=random.uniform(0, 100),
                timestamp=datetime.utcnow()
            ))

        db.bulk_save_objects(metrics)  # Efficient bulk insert for metrics
        db.commit()
        logger.info("LLMs and metrics seeded successfully.")

    except Exception as e:
        logger.error("Error while seeding database: %s", str(e))
        db.rollback()


if __name__ == "__main__":
    db = next(get_db())
    seed_database(db)





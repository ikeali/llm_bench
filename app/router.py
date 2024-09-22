from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Metric
from .database import get_db
from .ranking import rank_llms
from .utils.api_key_manager import create_api_key
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/rankings/")
def get_rankings(metric_identifier: str, db: Session = Depends(get_db)):
    logger.info("Fetching rankings for metric: %s", metric_identifier)

    try:
        # Check for metric by name
        metric = db.query(Metric).filter(Metric.name == metric_identifier).first()
        
        # If not found, check by ID
        if not metric:
            try:
                metric_id = int(metric_identifier)
                metric = db.query(Metric).filter(Metric.id == metric_id).first()
            except ValueError:
                logger.warning("Invalid metric identifier: %s", metric_identifier)
                raise HTTPException(status_code=404, detail="Metric not found")

        if not metric:
            logger.warning("Metric not found: %s", metric_identifier)
            raise HTTPException(status_code=404, detail="Metric not found")

        rankings = rank_llms(metric.id, db=db)
        
        return {"metric": metric.name, "rankings": rankings}
    
    except Exception as e:
        logger.error("Error occurred while fetching rankings: %s", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/api-keys/")
def generate_key(user_id: int, db: Session = Depends(get_db)):
    try:
        api_key = create_api_key(user_id=user_id, db=db)
        return {"api_key": api_key.key}
    except Exception as e:
        logger.error("Error generating API key for user %s: %s", user_id, str(e))
        raise HTTPException(status_code=500, detail="Error generating API key")

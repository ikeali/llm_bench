from fastapi import FastAPI, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from tenacity import retry, stop_after_attempt, wait_fixed
from .models import Metric, LLM
from .database import get_db
import logging
from .schemas import LLMCreate
# from fastapi import APIRouter
# from .ranking import router  
from .router import router  


from rq import Queue
from redis import Redis

redis_conn = Redis()
queue = Queue(connection=redis_conn)

app = FastAPI()
app.include_router(router)



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def create_llm_in_db(llm: LLMCreate, db: Session):
    logger.info("Attempting to create LLM...")
    
    existing_llm = db.query(LLM).filter(LLM.name == llm.name).first()
    if existing_llm:
        logger.warning("LLM with this name already exists: %s", llm.name)
        raise HTTPException(status_code=400, detail="LLM with this name already exists.")

    new_llm = LLM(name=llm.name, description=llm.description)
    db.add(new_llm)
    db.commit()
    db.refresh(new_llm)

    logger.info("Successfully created LLM: %s", new_llm.name)
    return new_llm


@app.post("/llms/")
def create_llm(llm: LLMCreate, db: Session = Depends(get_db)):
    # Enqueue the creation of the LLM
    queue.enqueue(create_llm_in_db, llm, db)
    return {"message": "LLM creation in progress"}


@app.get("/")
def read_root():
    return {"Hello": "This is just a test"}

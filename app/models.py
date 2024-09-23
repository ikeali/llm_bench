from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker,relationship
from sqlalchemy.sql import func
from datetime import datetime
from decouple import config
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()

class LLM(Base):
    __tablename__ = 'llms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(String(500))

    def __repr__(self):
        return f"<LLM(name={self.name})>"


class Metric(Base):
    __tablename__ = 'metrics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return f"<Metric(name={self.name})>"


class SimulationResult(Base):
    __tablename__ = 'simulation_results'

    id = Column(Integer, primary_key=True, autoincrement=True)
    llm_id = Column(Integer, ForeignKey('llms.id'), nullable=False)
    metric_id = Column(Integer, ForeignKey('metrics.id'), nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=func.now())

    llm = relationship("LLM", backref="simulation_results")
    metric = relationship("Metric", backref="simulation_results")

    def __repr__(self):
        return f"<SimulationResult(llm={self.llm_id}, metric={self.metric_id}, value={self.value})>"



class APIKey(Base):
    __tablename__ = 'api_keys'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    key = Column(String(64), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)
    
    user = relationship("User", back_populates="api_keys")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    
    api_keys = relationship("APIKey", back_populates="user")



DATABASE_URL = config('DATABASE_URL')

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()
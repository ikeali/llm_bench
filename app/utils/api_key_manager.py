import secrets
from sqlalchemy.orm import Session
from app.models import APIKey  
from datetime import datetime, timedelta

def generate_api_key() -> str:
    return secrets.token_hex(32)

def create_api_key(user_id: int, db: Session, expires_in_days: int = None) -> APIKey:
    key = generate_api_key()
    expiration_date = None
    if expires_in_days:
        expiration_date = datetime.utcnow() + timedelta(days=expires_in_days)
    
    api_key = APIKey(user_id=user_id, key=key, expires_at=expiration_date)
    db.add(api_key)
    db.commit()
    db.refresh(api_key)
    return api_key

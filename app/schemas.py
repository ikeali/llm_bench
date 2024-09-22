from pydantic import BaseModel

class LLMCreate(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True




from pydantic import BaseModel, Field
import Models
from Database import engine, SessionLocal
from sqlalchemy.orm import Session

Models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal
        yield db
    finally:
        db.close()

class Store_data(BaseModel):
    launch_time: str = Field(min_length = 1)
    duration_time: str = Field(min_length = 1)
    start_value: int = Field()
 

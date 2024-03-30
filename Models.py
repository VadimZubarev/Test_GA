from sqlalchemy import Column, Integer, String
from Database import Base


class Counter_data(Base):
    __tablename__ = "data_counter"

    id = Column(Integer, primary_key = True, index=True)
    launch_time = Column(String)
    duration_time = Column(String)
    start_value = Column(Integer)
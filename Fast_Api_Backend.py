import uvicorn
from fastapi import FastAPI, Depends
from Robot import Robot
from Counter import Counter
import asyncio
from Store_data import get_db, Store_data
import Models
from sqlalchemy.orm import Session
from Time_manager import Cur_time
from Database import SessionLocal


app = FastAPI()

def add_data():
    db = SessionLocal()
    counter_data_model = Models.Counter_data()
    counter_data_model.start_value = Store_data.start_value
    counter_data_model.duration_time = Store_data.duration_time
    counter_data_model.launch_time = Store_data.launch_time

    db.add(counter_data_model)
    db.commit()

@app.get('/RobotStatus')
async def get_status():
    robot_status = Robot.get_robot_status()
    print(Robot.get_robot_status())
    return {"Robot status" : robot_status}

@app.get('/Data')
async def read_data(db: Session = Depends(get_db)):
    return db.querry(Models.Data_counter).all()

@app.post('/StartRobot')
async def start_robot(start_value: int = 0):
    Cur_time.set_cur_time()
    Cur_time.start_time = Cur_time.now
    Store_data.launch_time = Cur_time.start_time
    Counter.counter = start_value
    Store_data.start_value = start_value
    Robot.is_running = True
    await Robot.increase_counter()
    return {"Satatus" : "Robot started"}

@app.post('/StopRobot')
async def stop_robot():
    Robot.is_running = False
    Cur_time.set_cur_time()
    Cur_time.end_time = Cur_time.now
    Store_data.duration_time = str(Cur_time.end_time - Cur_time.start_time)
    add_data()
    return {"Satatus" : "Robot stopped"}

def load_server():
    uvicorn.run("Fast_Api_Backend:app", host = '127.0.0.1', port = 8000, reload = True)


import uvicorn
from fastapi import FastAPI
from Robot import Robot
from Counter import Counter
import asyncio


app = FastAPI()

@app.get('/RobotStatus')
async def get_status():
    robot_status = Robot.get_robot_status()
    print(Robot.get_robot_status())
    return {"Robot status" : robot_status}

@app.post('/StartRobot')
async def start_robot(start_value: int = 0):
    Counter.counter = start_value
    Robot.is_running = True
    await Robot.increase_counter()
    return {"Satatus" : "Robot started"}

@app.post('/StopRobot')
async def stop_robot():
    Robot.is_running = False
    return {"Satatus" : "Robot stopped"}

def load_server():
    uvicorn.run("Fast_Api_Backend:app", host = '127.0.0.1', port = 8000, reload = True)
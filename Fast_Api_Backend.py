import uvicorn
from fastapi import FastAPI
from Robot import robot
from Robot import RobotStatus
from Robot import counter
import asyncio

app = FastAPI()

@app.get("/robot/status")
async def get_robot_status():
    robot_status = RobotStatus.running
    if robot_status:
        robot_counter = await robot.counter
        return {"status": robot_status, "counter": robot_counter}
    else:
        return {"status": robot_status}

@app.post("/robot/start")
async def start_robot():
    RobotStatus.running = True
    await robot()
    robot_counter = counter
    return {"message": "Robot started"}

@app.post("/robot/stop")
async def stop_robot():
    RobotStatus.running = False
    return {"message": "Robot stopped"}


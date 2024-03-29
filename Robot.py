import asyncio

counter = 0

class RobotStatus:
    running = False

async def robot():
    global counter
    while RobotStatus.running:
        print(counter)
        counter += 1
        await asyncio.sleep(1)

robot_task = asyncio.create_task(robot())
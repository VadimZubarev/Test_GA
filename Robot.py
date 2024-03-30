from Counter import Counter
import asyncio

class Robot:
    is_running = False

    async def increase_counter():
        while Robot.is_running:
            print(Counter.counter)
            Counter.counter += 1
            await asyncio.sleep(1)
    
    def get_robot_status():
        return Robot.is_running
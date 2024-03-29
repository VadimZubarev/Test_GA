import asyncio
import Robot

i = 0

async def main():
    while(True):
        task = asyncio.create_task(Robot())
        return_value = await task
        print(return_value)

#asyncio.run(main())
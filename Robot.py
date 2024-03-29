import asyncio

async def Robot():
    global i
    await asyncio.sleep(20)
    i += 1
    return i
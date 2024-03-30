import asyncio
from Robot import Robot
from Fast_Api_Backend import load_server

def main():
    asyncio.create_task(load_server())

if __name__ == '__main__':
    asyncio.run(main())

import asyncio


async def long_running_task():
    await asyncio.sleep(10)

async def main():
    try:
        await asyncio.wait_for(long_running_task(), timeout=5)
    except asyncio.TimeoutError:
        print("The task took too long!")

asyncio.run(main())



async def task():
    try:
        while True:
            print("Running...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Task was cancelled")

async def main():
    t = asyncio.create_task(task())
    await asyncio.sleep(3)
    t.cancel()
    await t

asyncio.run(main())


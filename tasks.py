import asyncio
import time

start = time.time()

async def greet(text):
    print(text)
    await asyncio.sleep(4)

async def main():
    print('Hello')
    task1 = asyncio.create_task(greet('How are you?'))
    print('Jim')


asyncio.run(main())
print(f'Finished in {time.time() - start}')
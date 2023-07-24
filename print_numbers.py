import asyncio
import time

start = time.time()

async def fetch():
    print('Start fetching')
    await asyncio.sleep(2)
    print('End fetching')
    return 'Done'

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(.25)

async def main():
    tasks = [asyncio.create_task(fetch()),
             asyncio.create_task(print_numbers())]
    
    value = await tasks[0]
    print(value)
    await tasks[1]

asyncio.run(main())
print(f'Finished in {time.time() - start}')
import asyncio
import os
from random import randint
import time

COEFF = 0.01


async def do_some_work(name, *tasks):
    times = [(tasks[0], tasks[1]), (tasks[2], tasks[3])]
    for n, (t1, t2) in enumerate(times, 1):
        print(f"{name} started the {n} task.")
        await asyncio.sleep(COEFF * t1)
        print(f"{name} moved on to the defense of the {n} task.")
        await asyncio.sleep(COEFF * t2)
        print(f"{name} completed the {n} task.")
        if n == 1:
            print(f"{name} is resting.")
            await asyncio.sleep(COEFF * 5)


async def interviews(*data):
    tasks = []
    for i in data:
        tasks.append(asyncio.create_task(do_some_work(*i)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews(*data))
    print(time.time() - t0)

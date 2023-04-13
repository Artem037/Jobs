import asyncio
import os
from random import randint
import time

COEFF = 0.01


async def do_some_work(name, *tasks):
    times = [(tasks[0], tasks[1], tasks[2], tasks[3])]
    for n, (t1, t2, t3, t4) in enumerate(times, 1):
        print(f"{name} started the {n} task.")
        print(f"{name} started the {n + 1} task.")
        await asyncio.sleep(COEFF * t1 + COEFF * t3)

        print(f"{name} moved on to the defense of the {n} task.")
        await asyncio.sleep(COEFF * t2)
        print(f"{name} completed the {n} task.")

        print(f"{name} moved on to the defense of the {n + 1} task.")
        await asyncio.sleep(COEFF * t4)
        print(f"{name} completed the {n + 1} task.")


async def interviews_2(*data):
    tasks = []
    for i in data:
        tasks.append(asyncio.create_task(do_some_work(*i)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews_2(*data))
    print(time.time() - t0)

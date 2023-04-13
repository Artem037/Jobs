import asyncio
import os
import time

COEFF = 0.01


async def buy_gift(name, v1, v2):
    print(f'Buy {name}')
    time.sleep(v1 * COEFF)
    await asyncio.sleep(COEFF * v2)
    print(f'Got {name}')


async def stop(i, t1, t2):
    print(f'Buying gifts at {i} stop')
    temp = sorted([x for x in gifts if x[1] + x[2] <= t1], key=lambda y: -(y[1] + y[2]))
    task = []
    res = t1
    for gift1 in temp:
        g_t1, g_t2 = gift1[1], gift1[2]

        if res - g_t1 - g_t2 >= 0:
            task.append(asyncio.create_task(buy_gift(*gift1)))
            res -= g_t1 + g_t2
            gifts.remove(gift1)
    await asyncio.gather(*task)
    print(f'Arrive from {i} stop')
    time.sleep(t2 * COEFF)


async def gift_def():
    task = []
    for item in gifts:
        task.append(asyncio.create_task(buy_gift(*item)))
    await asyncio.gather(*task)


def main():
    for i, ost in enumerate(stops, 1):
        asyncio.run(stop(i, *ost))
    if gifts:
        print('Buying gifts after arrival')
        asyncio.run(gift_def())


if __name__ == '__main__':
    stops = []
    stop_inp = input()
    while stop_inp:
        stops.append(tuple(map(int, stop_inp.split())))
        stop_inp = input()

    gifts = []
    gift = input()
    while gift:
        name, v1, v2 = gift.split()
        gifts.append((name, int(v1), int(v2)))
        gift = input()
    main()

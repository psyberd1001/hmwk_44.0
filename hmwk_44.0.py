import time
import asyncio

async def start_strongman(name, power):
    shar = 5
    time_sleep = 6
    time_sleep_end = time_sleep - power
    print(f'Силач {name} начал соревнование')
    for i in range(1, shar + 1):
        await asyncio.sleep(time_sleep_end)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач - {name} закончил соревнование!')

async def start_tournament():
    a1 = start_strongman('Kaptain Americ', 5)
    b1 = start_strongman('Nick Fiuri', 1)
    c1 = start_strongman('Halk', 4)
    await a1
    await b1
    await c1

async def main():
    print('start')
    #task1 = asyncio.create_task(start_tournament())
    task2 = asyncio.create_task(start_strongman('Kaptain Americ', 5))
    task3 = asyncio.create_task(start_strongman('Nick Fiuri', 1))
    task4 = asyncio.create_task(start_strongman('Halk', 4))
    await task2
    await task3
    await task4
    print('end')

asyncio.run(main())
import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) # Simulate a network request or IO operation
    # Return some data as a result
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Run coroutines concurrently and gather their return values
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

    # Process the results
    for result in results:
        print(f"Received reuslt: {result}")


asyncio.run(main())

"""
Ну короче он говорит в этом примере, что существует функция собиратель gather,
который все запускает и все собирает в один лист
но его главный минус в том, что он не обрабатывает ошибки, т.е. может вернуть в лист ошибку
поэтому следующий пример является более предпочтительным
"""
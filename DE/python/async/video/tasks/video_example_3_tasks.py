import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) # Simulate a network request or IO operation
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # After the Task Group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())

# Более предпочтительный способ выполнение асинхронна, ведь в TaskGroup есть обработка ошибок
# Работает это код так: В контекстном менеджере выполняется все такси и затем только после завершения
# Всех тасков он выходит из контексного менеджера и все выполнялсоь при этом ассинхронно
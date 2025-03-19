import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)
    # Set the result of the future
    future.set_result(value)
    print(f"Set the future's result to: {value}")

async def main():
    # Create a future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # Shedule setting the future's result
    asyncio.create_task(set_future_result(future, "Future result in ready"))

    # Wait for the future's result
    result = await future
    print(f"Received the future's result: {result}")

asyncio.run(main())

# На самом деле ничего не понял, ну он как-будто бы сказал это ненастллько важно,
# Вот работает future по-другому, future - это обещание выполнение
import asyncio

#Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print("Data fetched")
    return {"data": "Some data"} # Return some data

#Define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    # Await the fetch_data corouitne, pausing executin if main until fetch_data completes
    result = await task
    print(f"Received result: {result}")
    print("End of main coroutine")

asyncio.run(main())


# Рассказал, что очень важно понимать, что корутина не будет выполнена пока
# не будет выполнение действие await или помещена в какую-нибуждь стркуктуру tasks
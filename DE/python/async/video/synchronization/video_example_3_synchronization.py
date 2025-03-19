import asyncio

async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")

async def setter(event):
    await asyncio.sleep(2) # Simulate doing some work
    event.set()
    print("event has been set!")

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())

# Ну короче такая же крутая штука, используется как флаг, говорим wait и оно ждет пока будет set и затем идет дальше
# Он еще что-то упомянул о condition, но не разобрал
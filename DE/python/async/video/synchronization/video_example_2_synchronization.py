import asyncio

async def access_resourse(semaphore, resource_id):
    async with semaphore:
        # Simulate accesing a limited resource
        print(f"Accessing resource {resource_id}")
        await asyncio.sleep(1) # Simulate work with the resource
        print(f"Releasing resource {resource_id}")

async def main():
    semaphore = asyncio.Semaphore(5) # Allow 2 concurrent accesses
    await asyncio.gather(*(access_resourse(semaphore, i) for i in range(5)))

asyncio.run(main())


# Ну короче это тоже очень классная штука, в предедущем случае event loop мог одну
# А Semaphore позволяет выставлять какому количеству мы даем доступ, чтобы не перегружать системы
# т.е. больше одного дновременно могут делать операцию в lock
# Тоже очень классная штука
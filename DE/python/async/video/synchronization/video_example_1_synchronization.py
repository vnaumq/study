import asyncio

# A shared variable
shared_resourse = 0

# An asyncio Lock

lock = asyncio.Lock()

async def modify_shared_resourse():
    global shared_resourse
    async with lock:
        # Critical section starts
        print(f"Resourse before modification: {shared_resourse}")
        shared_resourse +=1 # Modify the shared resourse
        await asyncio.sleep(1) # Simulate an IO operation
        print(f"Resource atfer modification: {shared_resourse}")
        # Critical section ends

async def main():
    await asyncio.gather(*(modify_shared_resourse() for _ in range(5)))

asyncio.run(main())

# Очень importmant штука, типо если у нас одновременно выполняется, несколько задач, то вот это lock
# блокирует, чтобы одновременно выполнялась вот этот контекстный менеджер
# т.е. он выполняется только у одного, а затем у следуещего и так далее,
# Автор привел пример связанный с работой в БД, где одновременные результат может выдать ошибку или
# Некорректный результат
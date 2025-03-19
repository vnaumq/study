import aiohttp
import asyncio
import time


async def fetch(session, url:str):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            return {'error': f'Failed to fetch{url}, status: {response.status}'}

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/get",
    "https://httpbin.org/get"
    ]
    start_time = time.time()
    results = asyncio.run(fetch_all(urls))
    end_time = time.time()
    for i, result in enumerate(results):
        print(f"Response from {urls[i]}: {result}")

    print(f"Time taken {end_time - start_time:.2f} seconds")
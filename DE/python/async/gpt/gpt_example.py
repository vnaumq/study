import requests
import time

def fetch(url):
    try:
        response = requests.get(url)
        response.raise_for_status
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch {url}, error: {str(e)}"}

def fetch_all(urls):
    results = []
    for url in urls:
        results.append(fetch(url))
    return results

if __name__ == '__main__':
    urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/get",
    "https://httpbin.org/get"
    ]

    start_time = time.time()
    results = fetch_all(urls)
    end_time = time.time()

    print(f'Time taken: {end_time- start_time:.2f} seconds')
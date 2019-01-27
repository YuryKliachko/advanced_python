import asyncio
import aiohttp
import re
from urllib import request
import time
import threading

SOURCE_URL = 'https://www.python.org/downloads/source/'


def get_list_of_urls(source):
    response = request.urlopen(source).read().decode('utf-8')
    urls = re.findall(r'http.*tgz', str(response))
    return urls


async def async_download_one(session, url):
    async with session.get(url) as response:
        print(f"Start downloading from {url} asynchronously")
        result = await response.read()
        print(f'Downloaded from {url} asynchronously')
        return result


async def async_download_files(links):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(async_download_one(session, link)) for link in links[:25]]
        await asyncio.gather(*tasks)


def async_download(links):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_download_files(links))


def thread_download_one(link):
    print(f'Start downloading from {link} using a thread')
    request.urlretrieve(link)
    print(f'Downloaded from {link} using a thread')


def threads_download_files(links):
    threads = []
    for link in links[:25]:
        thread = threading.Thread(target=thread_download_one, args=(link,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def main():
    links = get_list_of_urls(SOURCE_URL)
    start = time.time()
    async_download(links)
    end = time.time()

    print(f'Time spent on downloading files asynchronously is {end - start}')

    start = time.time()
    threads_download_files(links)
    end = time.time()

    print(f'Time spent on downloading files using threads is {end - start}')


if __name__ == '__main__':
    main()

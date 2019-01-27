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
        print("Start downloading from {} asynchronously".format(url))
        result = await response.read()
        print('Downloaded from {} asynchronously'.format(url))
        return result


async def async_download_files(links):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in links:
            task = asyncio.ensure_future(async_download_one(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


def async_download(links):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_download_files(links))


def thread_download_one(link):
    print('Start downloading from {} using a thread'.format(link))
    request.urlretrieve(link)
    print('Downloaded from {} using a thread'.format(link))


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

    print('Time spent on downloading files \
    asynchronously is {}'.format(end - start))

    start = time.time()
    threads_download_files(links)
    end = time.time()

    print('Time spent on downloading \
    files using threads is {}'.format(end - start))


if __name__ == '__main__':
    main()

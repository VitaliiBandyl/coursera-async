import asyncio
import aiohttp
from time import time

url = 'https://loremflickr.com/320/240'


async def get_file(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_file(data)


def write_file(data):
    file_name = f'file-{(time() * 1000)}.jpeg'
    with open(f'D:\Python\Coursera\images\{file_name}', 'wb') as f:
        f.write(data)


async def main():
    t0 = time()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(get_file(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)
    print(time() - t0)

if __name__ == '__main__':
    asyncio.run(main())

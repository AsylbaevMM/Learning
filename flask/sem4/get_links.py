import requests
import asyncio
import aiohttp
import time
resp = requests.get('https://random.dog/woof.json')


async def get_link(i):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://random.dog/woof.json') as resp:
            result = await resp.json()
            return result['url'] + '\n'

async def main():
    tasks = []
    for i in range(100):
        task = asyncio.create_task(get_link(i))
        tasks.append(task)

    links = await asyncio.gather(*tasks)
    with open('links.txt', mode = 'a', encoding = 'utf-8') as file:
        file.writelines(links)

if __name__ == '__main__':
    for i in range(10):
        asyncio.run(main())
        time.sleep(10)
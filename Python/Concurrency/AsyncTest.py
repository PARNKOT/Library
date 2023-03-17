import asyncio
import aiohttp


async def request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://" + url) as response:
            print(f"{url} response status: {response.status}")


async def main():
    urls = [
        "google.com",
        "ya.ru",
        "microsoft.com",
        "linkedin.com",
    ]

    tasks = [asyncio.create_task(request(url)) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

from fastapi import FastAPI
import aiohttp
import asyncio

from . import config
from settings import settings


app = FastAPI()

URL = f"{settings.public_api_url}{settings.public_api_endpoint}"


async def request(session):
    async with session.get(URL) as response:
        return await response.text()


async def task():
    async with aiohttp.ClientSession() as session:
        tasks = [request(session) for _ in range(config.NO_OF_REQUESTS)]
        result = await asyncio.gather(*tasks)
        return result


@app.get('/')
async def fetch_beer_details():
    """
    This will hit the API will multiple requests concurrently and return the response together.
    """
    resp = await task()
    return resp

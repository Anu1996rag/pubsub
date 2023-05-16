import time

import aiohttp
import redis
from fastapi import FastAPI

from settings import settings


db = redis.Redis(
    host=settings.publisher_redis_url,
    port=settings.publisher_redis_port,
    decode_responses=True
)

app = FastAPI()

URL = f"http://{settings.publisher_url}:{settings.publisher_port}/"


async def request(session):
    async with session.get(URL) as response:
        return await response.json()


def publish_messages(messages):
    for message in messages:
        db.publish(settings.redis_channel, message)
        print(message)
        time.sleep(1)


async def task():
    async with aiohttp.ClientSession() as session:
        result = await request(session)
        # publish to queue
        publish_messages(result)


@app.get("/beers/publish")
async def get_beer_info():
    await task()

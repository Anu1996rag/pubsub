import time

import aiohttp
import redis
from fastapi import FastAPI

from settings import settings

db = redis.Redis(
    host=settings.subscriber_redis_url,
    port=settings.subscriber_redis_port,
    decode_responses=True
)

consumer = db.pubsub()

app = FastAPI()

URL = f"http://{settings.subscriber_url}:{settings.subscriber_port}/"


async def request(session):
    async with session.get(URL) as response:
        return await response.json()


def process_messages():
    consumer.subscribe(settings.redis_channel)
    for messages in consumer.listen():
        print(messages)
        time.sleep(0.5)


async def task():
    async with aiohttp.ClientSession() as session:
        await request(session)
        # publish to queue
        process_messages()


@app.get("/beers/subscribe")
async def get_beer_info():
    await task()

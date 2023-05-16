## PubSub Architecture using FastAPI and Redis

Introduction to PubSub or Event-driven architecture using Redis and FastAPI

Publisher tries to connect to external API asynchronously and fetches the response.

The response is then published on the REDIS CHANNEL.

This response/message is then further fetched by the subscriber by subscribing the REDIS CHANNEL.

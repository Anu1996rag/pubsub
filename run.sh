#!/bin/bash

source .env

uvicorn public_api.main:app --host "$BEER_DETAILS_API_URL" --port $BEER_DETAILS_API_PORT &
uvicorn publisher.publisher:app --host "$PUBLISHER_URL" --port $PUBLISHER_PORT &
uvicorn subscriber.subscriber:app --host "$SUBSCRIBER_URL" --port $SUBSCRIBER_PORT &
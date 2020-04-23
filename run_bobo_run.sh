#!/bin/sh

source env

docker run \
	--name bobo_runner \
	-v $(pwd):/app \
	--workdir /app \
	-e TOKEN=${TOKEN}
	-e CHAT_ID=${CHAT_ID}
	python:3.8 /app/entry.sh

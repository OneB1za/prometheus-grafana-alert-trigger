#!/bin/bash

# Имя контейнера
CONTAINER_NAME="django-github-app"

# Список URL-ов для запросов (указываем пути без http://, так как будем выполнять их внутри контейнера)
URLS=(
    "http://127.0.0.1:8000/slow/"
    "http://127.0.0.1:8000/usual/"
    "http://127.0.0.1:8000/random/"
)

# Таймаут между запросами (0.3 секунды)
SLEEP_TIME=0.3

echo "Request to: $CONTAINER_NAME"

while true; do
    for URL in "${URLS[@]}"; do
        RESPONSE=$(docker exec "$CONTAINER_NAME" curl -s -m 10 -o - -w "%{http_code}" "$URL")
        HTTP_STATUS=$(echo "$RESPONSE" | tail -n1)
        RESPONSE_BODY=$(echo "$RESPONSE" | head -c 35)

        echo "Request to $URL: $HTTP_STATUS | $RESPONSE_BODY"
    done
    sleep "$SLEEP_TIME"
done
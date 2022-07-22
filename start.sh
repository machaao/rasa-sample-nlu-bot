# Starts your action server and NLU with the MessengerX connector in Docker

cd app

rm -rf models

rasa train

rasa run actions --actions actions &

# Start rasa server with models dir
rasa run --model /app/models --enable-api \
        --debug \
        --endpoints /app/config/endpoints.yml \
        --credentials /app/config/credentials.yml \
        -p $PORT


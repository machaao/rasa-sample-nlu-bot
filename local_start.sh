# Start rasa action server
rasa run actions --actions actions &

# Start rasa core server
rasa run -m models --debug --endpoints config/endpoints.yml --credentials config/credentials.yml
:: Start rasa action server
start cmd /k rasa run --debug actions --actions actions

:: Start rasa core server
start cmd /k rasa run -m models --debug --endpoints config/endpoints.yml --credentials config/credentials.yml

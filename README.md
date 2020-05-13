# A sample RASA chatbot built using MACHAAO Platform
This RASA based Sample NLU chatbot intends to showcase various RCS-esque messaging options available on the Machaao Platform

![image](images/sample_rasa_machaao_bot.jpeg)

## Local Setup ##
* Download or clone this repository
           
* Get an api token via https://messengerx.io and place in the credential.yml
```
connectors.MachaaoConnector.MachaaoInputChannel:
    api_token: <YOUR API-TOKEN>
    base_url: "https://ganglia-dev.machaao.com"
```

### Train the sample model ###
Train your RASA model based on the sample set in the "data" folder
```
rasa train nlu 
```
### Start the RASA Action Service ###
Start your the action service either in a separate terminal or in the same tab as a background process.<br>

* In a separate terminal:
```
rasa run actions
```

* As a background process:
```
rasa run actions &
```

### Start RASA Core Service ###
Start rasa core and specify the custom connector.<br>
```
rasa run -m models --enable-api --cors “*” --connector "connectors.MachaaoConnector.MachaaoInputChannel"
```

### Install NGROK - For Dynamic DNS (Required) ###
* Install ngrok for your OS via https://ngrok.com/download.
* Run ngrok on port 5005 with the following command, and note the generated https url
```
ngrok http 5005
```

### Update your webhook ###
Update your bot url on MACHAAO with the NGROK url provided as shown below to continue development
```
curl --location --request POST 'https://ganglia-dev.machaao.com/v1/bots/<YOUR API-TOKEN> \
--header 'api_token: <YOUR API-TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "<YOUR URL>/webhooks/machaao/incoming",
    "description": "<YOUR BOT DESCRIPTION>",
    "displayName": "<YOUR BOT NAME>"
    }'
```

## Remote Setup via Heroku CLI (Optional) ##

* Apply for an api token from the machaao team and place it in the credential.yml.
* Install Heroku CLI for your OS
* Sign up for free on Heroku.
* Login to Heroku
```
heroku login
```
* Create a new app on Heroku and note down the app name.

* Push and deploy the docker image to Heroku.
```
heroku create
```

* Login to Heroku Container Service
```
heroku container:login
```

* Build the image and push to Container Registry
```
heroku container:push web
```
* Then release the image to your heroku app
```
heroku container:push release
```
* Open the app
```
heroku open
```




* Build locally (optional)
```
docker build -t herokurasa .
```

### Update your webhook ###
Update your bot url on MACHAAO with the heroku url as shown below to continue development
```
curl --location --request POST 'https://ganglia-dev.machaao.com/v1/bots/<YOUR API-TOKEN> \
--header 'api_token: <YOUR API-TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "<Your Bot Name>.herokuapp.com/webhooks/machaao/incoming",
    "description": "<YOUR BOT DESCRIPTION>",
    "displayName": "<YOUR BOT NAME>"
    }'
```

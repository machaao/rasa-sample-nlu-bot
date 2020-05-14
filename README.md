# A sample RASA chatbot built using MACHAAO Platform
This RASA based Sample NLU chatbot intends to showcase various RCS-esque messaging options available on the Machaao Platform

![image](images/sample_rasa_machaao_bot.jpeg)

## Running on Local ##
* Download or clone this repository
           
* You can acquire a FREE API token via https://messengerx.io or by [emailing us](mailto:connect@machaao.com) and replace it in the config/credential.yml
```
connectors.MachaaoConnector.MachaaoInputChannel:
    api_token: <YOUR API-TOKEN>
    base_url: "https://ganglia-dev.machaao.com"
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


### Re-Train the sample model ###
In order to re-train your RASA model based on the sample files provided in the "data" folder
```
rasa train
```

## Build local docker image ##
* Build locally docker image (optional)
```
docker build -t herokurasa .
```

## Running on Heroku (Optional) ##
* Install Heroku CLI for your OS
* We are assuming you have an heroku account.
* Assuming you have already acquired an api token from the machaao team, replace it in the config/credential.yml
* Login to Heroku
```
heroku login
```
* Create a new app on Heroku and note down your heroku app name

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
heroku container:release web
```
* Open the app
```
heroku open
```



### Update your webhook ###
Update your bot url on MACHAAO with the heroku url as shown below to continue development
```
curl --location --request POST 'https://ganglia-dev.machaao.com/v1/bots/<YOUR API-TOKEN> \
--header 'api_token: <YOUR API-TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "<Your_Heroku_App_Name>.herokuapp.com/webhooks/machaao/incoming",
    "description": "<YOUR BOT DESCRIPTION>",
    "displayName": "<YOUR BOT NAME>"
    }'
```

## Web Demo ##

A [RASA sample web demo](https://ganglia-dev.machaao.com/rasa.sample) has been made available for testing purposes

![image](images/sample_rasa_web_bot.png)


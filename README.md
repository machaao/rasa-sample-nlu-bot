[![Gitter](https://badges.gitter.im/messengerx-io/community.svg)](https://gitter.im/messengerx-io/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)  

## A sample RASA chatbot template using MACHAAO Chat Apps Platform and Heroku ##
The intent of the document is to provide with a quick and fast development setup guide for python developers looking to develop deeply personalized chat bots on Android & Web

This RASA based Sample NLU chatbot also intends to showcase various RCS-esque messaging options available on the Machaao Platform


![figure](images/sample_rasa_machaao_bot.jpeg)


## Web SDK Demo ##
A [RASA sample web demo](https://dev.messengerx.io/rasa.sample) has been made available for testing purposes

![figure](images/sample_rasa_web_bot.png)

## Run on Local (from source) ##
* Download or clone this repository
```
git clone git@github.com:machaao/rasa-sample-nlu-bot.git

cd rasa-sample-nlu-bot
```

* Install requirements
```bash
pip install -r requirements.txt
```

## Get your FREE API Key ##
* You can acquire a FREE API Key via https://messengerx.io 
or by [emailing us](mailto:connect@machaao.com) and replace it in the config/credentials.yml
```
connectors.MachaaoConnector.MachaaoInputChannel:
    api_token: <YOUR API-TOKEN>
    base_url: "https://ganglia-dev.machaao.com"
```

### Start the RASA Action Service ###
Start your the action service either in a separate terminal or in the same tab as a background process.<br>

* In a separate terminal:
```
rasa run actions --actions actions
```

* Or as a background process:
```
rasa run actions --actions actions &
```

### Start RASA Core Service ###
Start rasa core and specify the custom connector.<br>
```
rasa run -m models --debug --endpoints config/endpoints.yml --credentials config/credentials.yml --enable-api --cors “*” --connector "connectors.MachaaoConnector.MachaaoInputChannel"
```

### Using Machaao tunnel to expose PORT (Required) ###
* Run tunnel on port 5005 with the following command, and note the generated https url
```
machaao tunnel -p 5005 -t <Chatbot-Api-Token>
```

### Update your webhook ###
Update your bot Webhook URL on [MessengerX.io Portal](https://portal.messengerx.io) with the url provided as shown below to continue development
```
Webhook Url: <TUNNEL-URL>/webhooks/machaao/incoming
```

### Test your bot:
Visit: ```https://dev.messengerx.io/<bot-name>```


### Re-Train the Sample Model after changes ###
In order to re-train your RASA model based on the sample files provided in the "data" folder
```
rm -rf models/*
rasa train --domain domain.yml
```



## Run on Heroku ##
We are assuming you have access to a [heroku account](https://heroku.com)
and have installed heroku command line client for your OS.

### Login to Heroku ###
```
heroku login
```

Create a new app on Heroku and note down your heroku app name

### Push and deploy the docker image to Heroku ###
```
heroku create
```

### Build the docker image ###
```
docker build -t herokurasa .
```

### Login to Heroku Container Service ###
```
heroku container:login
```

### Push to Container Registry ###
```
heroku container:push web
```
### Release the image to your heroku app ###
```
heroku container:release web
```
### Open the heroku app or open the logs to confirm ###
```
heroku open
heroku logs --tail
```

### Update your webhook ###
Update your bot Webhook URL on [MessengerX.io Portal](https://portal.messengerx.io) with the heroku app url
```
Webhook Url: <YOUR-RASA-SERVER-URL>/webhooks/machaao/incoming
```

* You can run the code as it is, and it will use the provided Sample Token.

## Android Sample App Screenshot ##
Screenshot of the sample RASA chatbot running via our Android SDK

![figure](images/sample_rasa_android_bot.png)

## SDK Integration Guide ##
Please follow the SDK guide along with android + web integration sample @ https://github.com/machaao/machaao-samples

## Note ##
Please not that this document isn't mean to be use as a guide for production environment setup and nor it's intended for that purpose.


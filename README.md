[![Gitter](https://badges.gitter.im/messengerx-io/community.svg)](https://gitter.im/messengerx-io/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)  

## A sample RASA chatbot template using MACHAAO and Heroku ##
The intent of the document is to provide with a quick and fast development setup guide for python developers looking to develop deeply personalized chat bots on Android & Web

This RASA based Sample NLU chatbot also intends to showcase various RCS-esque messaging options available on the Machaao Platform

![figure](images/sample_rasa_machaao_bot.jpeg)

## Requirements ##
* MessengerX.io API Token
* Rasa 3.0.4
* Python 3.7, 3.8 Only
* Docker (Optional for Remote Deployment)
* Heroku Account (Optional for Remote Deployment)

## Get your FREE API Key ##
* You can acquire a FREE API Key via https://messengerx.io 
or by [emailing us](mailto:connect@machaao.com) and replace it in the config/credentials.yml
```
connectors.MachaaoConnector.MachaaoInputChannel:
    api_token: <YOUR API-TOKEN>
    base_url: "https://ganglia.machaao.com"
```

## Run on Local Machine (from source) ##
* Download or clone this repository
```
git clone git@github.com:machaao/rasa-sample-nlu-bot.git

cd rasa-sample-nlu-bot
```

* Setup a dev virtual environment on your local machine
```
python3 -m venv ./dev
source ./dev/bin/activate
```

* Setup a dev virtual environment on your local machine (Windows)
```
python3 -m venv ./dev
.\dev\Scripts\activate
```

* Install requirements
```bash
pip install -r requirements.txt
```
### For M1 Macbook (Conda maybe required - Instructions Pending) ####
Refer to 
https://forum.rasa.com/t/an-unofficial-guide-to-installing-rasa-on-an-m1-macbook/51342

Tensorflow setup instructions: https://developer.apple.com/metal/tensorflow-plugin/

### Start the RASA Action Core Service ###
Start the rasa action service(background) and core service in the terminal. 
```
chmod +x local_start.sh
./local_start.sh
```

### Start RASA Action and Core Service (Windows) ###
Start the rasa action and core services in separate terminals.<br>
```
call local_start.bat
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
Visit: ```https://messengerx.io/<bot-name>```


### Re-Train the Sample Model after changes ###
In order to re-train your RASA model based on the sample files provided in the "data" folder
```
rm -rf models/*
rasa train --domain domain.yml
```

## Web SDK Demo ##
[Bella by VisitorPlans.com](https://messengerx.io/vp) - Powered by RASA + MessengerX.io

![figure](images/sample_rasa_web_bot.png)

## Run on Heroku (Optional - Not Production Setup) ##

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
docker build -t rasa .
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


## Note ##
* Please note that this document isn't mean to be use as a guide for production environment setup and nor it's intended for that purpose.
* Running the RASA chat app on Heroku requires a 2X Instance.
* Please [contact us](mailto:connect@machaao.com) for your Android APK

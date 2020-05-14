# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import requests
import json
import yaml
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import os.path
abs_path = os.path.abspath(os.path.dirname(__file__))

base_url = ""
api_token = ""

path = os.path.join(abs_path, "../config/credentials.yml")

with open(path) as file:
    credentials = yaml.load(file, Loader=yaml.FullLoader)
    base_url = credentials["connectors.MachaaoConnector.MachaaoInputChannel"]["base_url"]
    api_token = credentials["connectors.MachaaoConnector.MachaaoInputChannel"]["api_token"]
    file.close()

class ActionSendText(Action):

    def name(self) -> Text:
        return "action_send_text"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="This is a sample text from actions")

        return []

class ActionSendImage(Action):

    def name(self) -> Text:
        return "action_send_image"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_image_url("https://i.imgur.com/nGF1K8f.jpg")

        return []

class ActionSendCarousel(Action):

    def name(self) -> Text:
        return "action_send_carousel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        elements = [{"title": "Sample Title 1",
                    "subtitle": "Sample Subtitle 1",
                     "image_url": "https://i.imgur.com/nGF1K8f.jpg"
                     },
                    {
                        "title": "Sample Title 2",
                        "subtitle": "Sample Title 2",
                        "image_url": "https://i.imgur.com/nGF1K8f.jpg"
                    },
                    {
                       "title": "Sample Title 3",
                       "subtitle": "Sample Title 3",
                       "image_url": "https://i.imgur.com/nGF1K8f.jpg"
                    }
                    ]
        dispatcher.utter_custom_json(elements)
        return []

class ActionSendButtons(Action):

    def name(self) -> Text:
        return "action_send_buttons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = "Sample Button Replies"
        buttons = [{'title': 'Test Sample Text', 'payload': 'Sample Text', 'content_type': 'text'},
                   {'title': 'Test Sample Image', 'payload': 'Sample Image', 'content_type': 'text'},
                   {'title': 'Test Sample Carousel', 'payload': 'Sample Carousel', 'content_type': 'text'}]
        dispatcher.utter_button_message(text, buttons)
        return []


def add_or_remove_tag(sender_id:str,on_off:int) -> None:
    """
    :param sender_id: Used to specify which user to tag. You can get this from tracker
    :param on_off: activate tags by passing 1, deactivate by passing 0
    :return:
    """

    tag = "Your-Tag-Name"
    display_name = "Your Display Name"
    API_ENDPOINT = base_url + "/v1/users/tag/" + sender_id

    print("Tag ENDPOINT")
    print(API_ENDPOINT)

    headers = {
        "api_token": api_token,
        "Content-Type": "application/json"
    }
    payload = {
            "tag": tag,
            "source": "firebase",
            "status": on_off,
            "displayName": display_name
    }

    requests.post(url=API_ENDPOINT, data=json.dumps(payload), headers=headers)
    return None


def send_announcement(tag:str,message:str) -> None:
    """
    :param tag: Specifies which subset of users you would like to message
    :param message: The message you would like to send
    :return:
    """

    API_ENDPOINT = base_url + "/v1/messages/announce"

    headers = {
        "api_token": api_token,
        "Content-Type": "application/json"
    }

    payload = {
        "tags": [tag],
        "identifier": "BROADCAST_FB_TEMPLATE_GENERIC",
        "notificationType": "REGULAR",
        "source": "firebase",
        "message": {
            "text": message
        }
    }
    requests.post(url=API_ENDPOINT, data=json.dumps(payload), headers=headers)
    return None

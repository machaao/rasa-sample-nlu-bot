import logging
import inspect
from sanic import Blueprint, response
from sanic.request import Request
from typing import Text, List, Dict, Any, Optional, Callable, Awaitable
from rasa.core.channels.channel import UserMessage, OutputChannel, InputChannel
import jwt
import json
import requests

logger = logging.getLogger(__name__)
api_token = ""
base_url = ""


class MachaaoInputChannel(InputChannel):
    """A custom http input channel for MACHAAO Platform
    "" Credits: Darren Yau (darren@machaao.com)
    This implementation is the basis for a custom implementation of a chat
    frontend. You can customize this to send messages to RASA Core and
    retrieve responses from the agent."""

    @classmethod
    def name(cls):
        return "machaao"

    @classmethod
    def from_credentials(cls, credentials):
        global api_token
        api_token= credentials.get("api_token")
        global base_url
        base_url= credentials.get("base_url")
        return cls()

    async def _extract_sender(self, req) -> Optional[Text]:
        return req.headers["user_id"]

    def _extract_message(self, req):
        """
        Decrypts the request body, and parses the incoming message
        """
        decoded_jwt = None
        body = json.loads(req.body)

        logger.info("raw json: " + str(req.body))

        if body and body["raw"]:
            decoded_jwt = jwt.decode(body["raw"], api_token, algorithm='HS512')
        text = decoded_jwt["sub"]
        if type(text) == str:
            text = json.loads(decoded_jwt["sub"])

        logger.info("decoded json: " + str(text))

        return text["messaging"][0]["message_data"]["text"]

    def blueprint(self, on_new_message: Callable[[UserMessage], Awaitable[None]]):
        custom_webhook = Blueprint(
            "custom_webhook_{}".format(type(self).__name__),
            inspect.getmodule(self).__name__,
        )

        @custom_webhook.route("/", methods=["GET"])
        async def health(request: Request):
            return response.json({"status": "ok"})

        @custom_webhook.route("/incoming", methods=["POST"])
        async def receive(request: Request):
            logger.info("incoming req")
            sender_id = await self._extract_sender(request)
            text = self._extract_message(request)
            collector = MachaaoOutputChannel()
            try:
                logger.info("incoming request -> forwarded")
                await on_new_message(
                    UserMessage(
                        text, collector, sender_id, input_channel=self.name()
                    )
                )
            except Exception:
                logger.exception(
                    "An exception occured while handling "
                    "user message '{}'.".format(text)
                )
            return response.text("Bot message delivered.")

        return custom_webhook


class MachaaoOutputChannel(OutputChannel):
    """
    defines several messaging types currently supported by the Machaao platform
    """
    def __init__(self) -> None:
        pass

    @classmethod
    def name(cls) -> Text:
        return "collector"

    async def send_text_message(
        self, recipient_id: Text, text: Text, **kwargs: Any
    ) -> None:
        API_ENDPOINT = base_url + "/v1/messages/send"

        logger.info("calling: " + API_ENDPOINT + " with text: " + text)

        headers = {
            "api_token": api_token,
            "Content-Type": "application/json"
        }

        data = {
            "users": [recipient_id],
            "identifier": "BROADCAST_FB_QUICK_REPLIES",
            "notificationType": "REGULAR",
            "source": "firebase",
            "message": {
                "text": text
            },
        }
        requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=headers)

    async def send_image_url(
        self, recipient_id: Text, image: Text, **kwargs: Any
    ) -> None:
        """Sends an image. Default will just post the url as a string."""
        API_ENDPOINT = base_url + "/v1/messages/send"
        # your source code here
        headers = {
            "api_token": api_token,
            "Content-Type": "application/json"
        }
        payload = {
            "users": [recipient_id],
            "identifier": "BROADCAST_FB_TEMPLATE_GENERIC",
            "notificationType": "REGULAR",
            "source": "firebase",
            "message": {
                "attachment": {
                    "type": "image",
                    "payload": {
                        "url": image
                    }
                }
            }
        }
        requests.post(url=API_ENDPOINT, data=json.dumps(payload), headers=headers)

    async def send_text_with_buttons(
        self,
        recipient_id: Text,
        text: Text,
        buttons: List[Dict[Text, Any]],
        **kwargs: Any,
    ) -> None:
        API_ENDPOINT = base_url + "/v1/messages/send"
        headers = {
            "api_token": api_token,
            "Content-Type": "application/json"
        }
        payload = {
            "users": [recipient_id],
            "identifier": "BROADCAST_FB_QUICK_REPLIES",
            "notificationType": "REGULAR",
            "source": "firebase",
            "message": {
                "text": text,
                "quick_replies": buttons
            }
        }
        requests.post(url=API_ENDPOINT, data=json.dumps(payload), headers=headers)

    # Used to send Carousel Messages
    async def send_custom_json(
        self, recipient_id: Text, json_message: Dict[Text, Any], **kwargs: Any
    ) -> None:
        API_ENDPOINT = base_url + "/v1/messages/send"
        headers = {
            "api_token": api_token,
            "Content-Type": "application/json"
        }

        payload = {
                "users": [recipient_id],
                "identifier": "BROADCAST_FB_TEMPLATE_GENERIC",
                "notificationType": "REGULAR",
                "source": "firebase",
                "message": {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": json_message
                        }
                    }
                }
        }
        requests.post(url=API_ENDPOINT, data=json.dumps(payload), headers=headers)
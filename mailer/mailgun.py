import logging
import requests


class Mailer:
    def __init__(self, api_key, site, api_loc='eu.'):
        self.api_key = api_key
        self.url = f"https://api.{api_loc}mailgun.net/v3/{site}/messages"

    def send(self, sender, recipient, subject, body, attachment):
        logging.debug(
            f"{sender}, {recipient}, {subject}, {body}, {attachment}")

        auth = ("api", self.api_key)
        data = {"from": sender,
                "to": [recipient],
                "subject": subject,
                "text": body}

        logging.debug(f"url: {self.url}, body: {body}")

        if attachment != None:
            requests.post(
                self.url,
                auth=auth,
                files=[("attachment", (attachment.get(
                    "filename"), attachment.get("content")))],
                data=data)
        else:
            requests.post(
                self.url,
                auth=auth,
                data=data)

import json
from urllib import response

import requests

from config.config import Config

config = Config()  # Init Config object.


class API:
    def __init__(self):
        self.host = config.host
        self.port = config.port
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json'}

    def get_statistic(self):
        response = self._make_get_statistic_request(
            host=self.host, port=self.port)
        content = self.serialize_response_content(content=response.content)
        return content

    def stop_attack(self, pk: str):
        response = self._make_stop_attack_request(
            host=self.host, port=self.port, pk=pk)
        content = self.serialize_response_content(content=response.content)
        return content

    def run_attack(self, user_id: int, phone: int):
        response = self._make_run_attack_request(
            host=self.host, port=self.port, user_id=user_id, phone=phone)
        content = self.serialize_response_content(content=response.content)
        return content

    def create_user(self, user_id: int, username: str, first_name: str, last_name: str):
        response = self._make_create_user_request(
            host=self.host, port=self.port, user_id=user_id, username=username, first_name=first_name, last_name=last_name)
        content = self.serialize_response_content(content=response.content)
        return content

    # Make request functions.

    def _make_get_statistic_request(self, **kwargs):
        url = r"http://{host}:{port}/api/get_statistic".format(
            **kwargs)
        response = requests.get(url=url, headers=self.headers)
        return response

    def _make_stop_attack_request(self, **kwargs):
        url = r"http://{host}:{port}/api/stop_attack/{pk}".format(
            **kwargs)
        response = requests.get(url=url, headers=self.headers)
        return response

    def _make_run_attack_request(self, **kwargs):
        url = r"http://{host}:{port}/api/run_attack/{user_id}/{phone}".format(
            **kwargs)
        response = requests.get(url=url, headers=self.headers)
        return response

    def _make_create_user_request(self, **kwargs) -> requests.Response:
        url = r"http://{host}:{port}/api/create_user/{user_id}/{username}/{first_name}/{last_name}".format(
            **kwargs)
        response = requests.get(url=url, headers=self.headers)
        return response

    def serialize_response_content(self, content) -> dict:
        return json.loads(content)

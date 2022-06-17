import os
from dataclasses import dataclass

import dotenv
from dotenv import load_dotenv, find_dotenv


@dataclass
class Config:
    token: str
    host: str
    port: int


    def __init__(self):
        load_dotenv(find_dotenv())
        self.set_config()

    def set_config(self):
        self.token = os.getenv("BOT_TOKEN")
        self.host = os.getenv("WEB_HOST")
        self.port = os.getenv("WEB_PORT")

    def change_value(self, key, value):
        os.environ[key] = value
        dotenv.set_key(dotenv.find_dotenv(), key, os.environ[key])
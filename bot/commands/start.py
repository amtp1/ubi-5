from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from objects import globals
from objects.globals import dp
from request.api import API

api = API()


@dp.message_handler(commands='start')
async def start(message: Message):
    locale = message.from_user.locale
    msg_chat = message.chat

    api.create_user(msg_chat.id, msg_chat.username,
                    msg_chat.first_name, msg_chat.last_name)

    if locale.language == "ru":
        keyboard_text = "Атаковать номер"
        message_text = "Привет! Я бот"
    else:
        keyboard_text = "Attack phone"
        message_text = "Hello! I'm bot"

    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text=keyboard_text)]
    ])
    return await message.answer(F"{message_text} - @{globals.bot_info.username}", reply_markup=reply_markup)

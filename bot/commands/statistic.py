from aiogram.types import Message

from objects.globals import dp
from request.api import API

api = API()


@dp.message_handler(commands='stat')
async def start(message: Message):
    response = api.get_statistic().get("statistic")
    all_users = response.get("all_users")
    last_login_users = response.get("last_login_users")
    stat_page: str = (f"<b>Статистика</b>\n"
                      f"<code>|--</code><i>Общее количество</i>: {all_users}\n"
                      f"<code>|--</code><i>Активные за день</i>: {last_login_users}\n")
    return await message.answer(stat_page)

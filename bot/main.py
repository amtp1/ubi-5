import asyncio
from re import A

from aiogram.types import Message
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from objects.globals import config
from objects import globals

from logger.logger import logger


async def main():
    globals.bot = Bot(token=config.token, parse_mode="HTML")
    globals.dp = Dispatcher(globals.bot, storage=MemoryStorage())

    globals.bot_info = await globals.bot.get_me()
    logger.info(
        F"Bot working! (@{globals.bot_info.username})", user_id=globals.bot_info.id)

    import commands

    await globals.dp.start_polling()

if __name__ == "__main__":
    try:
        main_loop = asyncio.get_event_loop()
        main_loop.run_until_complete(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped", user_id=globals.bot_info.id)

from aiogram.dispatcher.filters.state import StatesGroup, State

class Phone(StatesGroup):
    phone = State()
from aiogram.dispatcher.filters.state import StatesGroup, State

class Lists(StatesGroup):
    photo = State()
    desc = State()
    length = State()
    width = State()
    height = State()
    weight = State()
    contact_received = State()
    name_received = State()
    
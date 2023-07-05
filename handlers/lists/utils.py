from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))


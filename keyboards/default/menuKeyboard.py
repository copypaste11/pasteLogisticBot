from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=1)
buttons = [
    InlineKeyboardButton('Оставить заявку'),
    InlineKeyboardButton('Указать точные параметры груза')
]

menu.add(*buttons)

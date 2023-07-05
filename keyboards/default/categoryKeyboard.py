from typing import List
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard(categories: List[str]) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(0, len(categories), 2):
        if i+1 < len(categories):
            kb.add(KeyboardButton(categories[i]), KeyboardButton(categories[i+1]))
        else:
            kb.add(KeyboardButton(categories[i]))
    kb.add(KeyboardButton('🔙 Назад'))
    return kb


categories = ['🔌 Электроника без АКБ', '🔋 Электроника с АКБ', '🏸 Спорт.инвентарь', '🏚 Хоз.товары', '👟 Обувь, одежда, сумки', '🚗  Автозапчасти', '🛠 Оборудование', '🛋 Мебель', '🧸 Игрушки', '🎮 Видеокарты', '🧵 Текстиль']
keyboard = get_keyboard(categories)

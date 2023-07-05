from aiogram import types

from loader import dp, bot

@dp.message_handler(commands='ouradresses')
async def ouradresses_handle(message: types.Message):
    text = ("Мы предлагаем международные перевозки из следующих стран:\n\n"
            " - Китай 🇨🇳\n"
            "Адрес:\n\n"
            " - Россия 🇷🇺\n"
            "Адрес:\n\n"
            " - Турция 🇹🇷\n"
            "Адрес:\n\n"
            " - Киргизстан 🇰🇬\n"
            "Адрес:\n\n"
            " - Юж. Корея 🇰🇷\n"
            "Адрес:\n\n"
            "  - ОАЭ🇦🇪\n"
            "Адрес:")
    
    await message.answer(text)
    
from aiogram import types

from loader import dp

@dp.message_handler(commands='cargoinsurance')
async def insurance_handler(message: types.Message):
    text = 'Мы сейчас работаем над этой командой'

    await message.answer(text)
    
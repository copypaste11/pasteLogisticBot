from aiogram import types

from loader import dp, bot

@dp.message_handler(commands='cargostatus')
async def cargostatus_handle(message: types.Message):
    text = ("Пункт <b>Статус груза</b> предназначен для проверки текущего состояния и местоположения груза по номеру отслеживания.\n\n"
            "Клиент может узнать, находится ли груз в пути, прошел ли он таможенный контроль, когда он будет доставлен и т.д.")
    
    await message.answer(text)
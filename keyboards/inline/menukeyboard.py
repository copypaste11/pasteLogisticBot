from aiogram import types

from loader import dp, bot

@dp.callback_query_handler(lambda query: query.data == 'menu')
async def handle_sea_button(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.asnwer(commands='bulkorder')
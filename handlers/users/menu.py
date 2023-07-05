from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from keyboards.default.menuKeyboard import menu
from keyboards.default.categoryKeyboard import get_keyboard, categories
from aiogram import types
from states.aboutProduct import Lists
from loader import dp, bot
from handlers.lists.utils import get_cancel

from aiogram import types
from loader import dp

menu = types.InlineKeyboardMarkup(row_width=1)
buttons = [
    types.InlineKeyboardButton(text='Оставить заявку', url='https://forms.gle/XhWxsSgd2gQ5QjgR8'),
    types.InlineKeyboardButton(text='Указать точные параметры груза', callback_data='utpg'),
]
menu.add(*buttons)

@dp.message_handler(commands='bulkorder')
async def show_menu(message: types.Message):
    await message.answer("Что нужно для расчета стоимости доставки из-за рубежа?\n\n"
                         "Для того, чтобы рассчитать примерную стоимость доставки до Узбекистана, необходимы следующие данные о грузе:\n\n"
                         " - общий объем и вес\n"
                         " - наименование товара\n"
                         " - брендовый товар или нет\n"
                         " - стоимость товара ,$\n\n"
                         "На основе этих данных мы сможем рассчитать примерную стоимость доставки.\n\n")
    
    await message.answer("Почему примерную?\n\n"
                         "Потому что, после упаковки груза его фактический вес и объем будут другими.\n\n"
                         "Также в данном расчёте не будут учтены рыночные сборы, стоимость упаковки и страховка.")
    
    await message.answer("Выберите откуда хотите доставить?", reply_markup=menu)

# @dp.callback_query_handler(lambda query: query.data == 'iu')
# async def handle_sea_button(callback_query: types.CallbackQuery):
#     await callback_query.answer()
#     await callback_query.message.answer('Выберите категорию:', reply_markup=categories)

# @dp.message_handler(text="Гуанчжоу 🇨🇳 - Узбекистан")
# async def send_link2(message: Message):
#     keyboard = get_keyboard(categories)
#     await message.answer('Выберите категорию:', reply_markup=buttons)


# @dp.message_handler(text="🔙 Назад")
# async def send_link3(message: Message):
#     await message.answer('Выберите откуда хотите доставить?', reply_markup=menu)


# # automatiove
# @dp.message_handler(Text(equals='🔌 Электроника без АКБ', ignore_case=True), state=None)
# async def bez_akb(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='🔋 Электроника с АКБ', ignore_case=True), state=None)
# async def s_akb(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='🏸 Спорт.инвентарь', ignore_case=True), state=None)
# async def sport_inventar(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='🏚 Хоз.товары', ignore_case=True), state=None)
# async def xoz_tovari(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='👟 Обувь, одежда, сумки', ignore_case=True), state=None)
# async def obuv_odejda_sumki(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='🚗  Автозапчасти', ignore_case=True), state=None)
# async def avto_zapchast(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='🛠 Оборудование', ignore_case=True), state=None)
# async def tech(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='🛋 Мебель', ignore_case=True), state=None)
# async def mebel(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='🧸 Игрушки', ignore_case=True), state=None)
# async def toys(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='🎮 Видеокарты', ignore_case=True), state=None)
# async def video_cards(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())


# @dp.message_handler(Text(equals='🧵 Текстиль', ignore_case=True), state=None)
# async def textile(message: types.Message) -> None:
#     await Lists.photo.set()
#     await message.answer('Пожалуйста, отправьте фотографию товара.',
#                          reply_markup=get_cancel())

from aiogram import types
from aiogram.dispatcher import FSMContext
from states.aboutProduct import Lists
from data.config import CHANNELS
from loader import dp, bot
from aiogram.types import ParseMode
from aiogram.types import Message
from handlers.lists.utils import get_cancel
from handlers.users.menu import menu
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(commands=['cancel'], state='*')
async def cancel(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await message.reply('Отменил!',
                        reply_markup=menu)
    await state.finish()


# Define message handlers for each state
@dp.message_handler(state=Lists.photo, content_types=['photo'])
async def step1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        photo_id = data['photo']

        for channel in CHANNELS:
            await bot.send_photo(chat_id=channel, photo=photo_id)
    await Lists.desc.set()
    await message.reply('A теперь отправьте описание пожалуйста.')

@dp.message_handler(lambda message: not message.photo, state=Lists.photo)
async def check_photo(message: types.Message):
    return await message.reply('Это не фотография!')


@dp.message_handler(state=Lists.desc)
async def step2(message: types.Message, state: FSMContext):
    desc = message.text
    await state.update_data(
        {
            'desc': desc
        }
    )
    await message.answer('Пожалуйста, отправьте длину товара.',
                         reply_markup=get_cancel())
    await Lists.next()


@dp.message_handler(state=Lists.length)
async def length_state(message: types.Message, state: FSMContext):
    length_state = message.text
    await state.update_data(
        {
            'length': length_state
        }
    )
    await message.reply('Пожалуйста, отправьте ширину товара в см.',
                        reply_markup=get_cancel())

    await Lists.width.set()


@dp.message_handler(state=Lists.width)
async def step5(message: types.Message, state: FSMContext):
    width_state = message.text
    await state.update_data(
        {
            'width': width_state
        }
    )
    await message.answer('Пожалуйста, введите высоту вашего товара в см.',
                         reply_markup=get_cancel())
    await Lists.height.set()


@dp.message_handler(state=Lists.height)
async def step6(message: types.Message, state: FSMContext):
    height_state = message.text
    await state.update_data(
        {
            'height': height_state
        }
    )
    await message.answer('Пожалуйста, введите массу вашего товара в кг',
                         reply_markup=get_cancel())
    await Lists.weight.set()


@dp.message_handler(state=Lists.weight)
async def weight_state(message: types.Message, state: FSMContext):
    weight_state = message.text
    await state.update_data(
        {
            'weight': weight_state
        }
    )

    data = await state.get_data()
    sendmessage = f" Фото товара: {data['photo']}\n" \
                  f" Описание товара: {data['desc']}\n" \
                  f" Высота: {data['length']}\n" \
                  f" Ширина: {data['width']}\n" \
                  f" Длина: {data['height']}\n" \
                  f" MACCA: {data['weight']}"
    await bot.send_message(chat_id=CHANNELS[0], text=sendmessage, parse_mode=ParseMode.HTML)
    await message.answer('Спасибо вам! Все ваши данные сохранены.\n\n'
                         'Если есть какие то не поладки или замечания будем рады обсудить с вами свяжитесь с нами - @kakoytamaneger\n\n'
                         'Вы можете нажать на /menu ещё раз если хотите добавить свой товар, удачи и хорошего настроения.', reply_markup=ReplyKeyboardRemove())
    await state.finish()

from aiogram import types
from aiogram.types import ContentTypes, ReplyKeyboardRemove
from aiogram.dispatcher.filters import CommandStart
from loader import dp, bot
from states.aboutProduct import Lists
from aiogram.dispatcher import FSMContext


@dp.message_handler(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    text = ("@logisticagency_bot — сервис логистических услуг\n\n"
            "<b>Главное</b>\n"
            "/help - показывает это сообщение\n\n"
            "<b>О нас</b>\n"
            "/aboutus — О нас\n"
            "/ouradresses — Наши адреса\n\n"
            "<b>Рассчитать стоимость доставк</b>\n"
            "/bulkorder — Оптовые расчёт\n"
            "/unitorder —  Расчёт в штучных объёмах\n\n"
            "<b>Статус груза и номера отслеживания</b>\n"
            "/cargostatus —  Статус груза\n"
            "/alltrackings  —  Все номера отслеживания\n\n"
            "<b>Страхование груза</b>\n"
            "/cargoinsurance — Страхование груза\n\n"
            "<b>Тарифы</b>\n"
            "/shippingrates — Тарифы доставки грузов (авиа, авто, морем и Ж/Д)\n\n"
            "Инструкция по применению бота\n"
            "/info — Инструкция по применению бота\n\n"
            "Если у вас есть замечания или предложения, будем рады обсудить их вместе в чате Optovka_uz @optovka_new\n\n"
            "Центр поддержки: @admin")

    await bot.send_message(chat_id=message.chat.id, text=text, parse_mode='HTML')

    await bot.send_message(chat_id=message.chat.id, text="Пожалуйста, отправьте свой контакт.\nЭто для того чтобы наши операторы связались с вами!", reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="📱 Отправить контакт", request_contact=True)
                ]
            ],
            resize_keyboard=True
        ))

    await Lists.contact_received.set()

@dp.message_handler(content_types=ContentTypes.CONTACT, state=Lists.contact_received)
async def process_contact(message: types.Message, state: FSMContext):
    contact = message.contact
    await state.update_data(contact=contact)

    await bot.send_message(chat_id=message.chat.id, text="Пожалуйста введите своё имя и фамилию.")

    await Lists.name_received.set()

@dp.message_handler(state=Lists.name_received)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    data = await state.get_data()
    contact = data.get('contact')

    await bot.send_message(chat_id=message.chat.id, text=f"Спасибо, {name}! Мы получили ваш контакт: {contact.phone_number}\n\n"
                           "Вы можите призывать команду /help для больше информации.", reply_markup=ReplyKeyboardRemove())

    await state.finish()

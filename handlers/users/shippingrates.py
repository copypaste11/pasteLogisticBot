from aiogram import types
from loader import dp, bot

from keyboards.inline import shipping

@dp.message_handler(commands='shippingrates')
async def shippingrates(messsage: types.Message):
    text = ("<b>Тарифы доставки Авиа</b>\n\n"
            "- Авиа 'Экспресс' - Кому срочно нужно доставить образцы\n"
            "- Авиа 'Посылка' - Доставка до вашего города\n"
            "- Авиа 'Стандарт'\n"
            "Доставка в Ташкент\n\n"
            "<b>Тарифы доставки морем</b>\n\n"
            "- Целый контейнер\n"
            "- от 300 кг\n"
            "- от 1000 кг\n\n"
            "<b>Тарифы доставки Ж/Д</b>\n\n"
            "- Целый контейнер\n"
            "- от 300 кг\n"
            "- от 1000 кг\n\n"
            "<b>Внимание! Цена указана с Таможенной очисткой</b>\n\n"
            "<b>Бесплатный расчет в течение 24 часов!</b>\n\n"
            "Хотите получить расчет доставки вашего груза – жмите на кнопку и оставляйте заявку, наш менеджер с вами свяжется.")

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton(text="Авиа ✈️", callback_data="air")
    button2 = types.InlineKeyboardButton(text="Mope 🚢", callback_data="sea")
    button3 = types.InlineKeyboardButton(text="Авто 🚛", callback_data="road")
    button4 = types.InlineKeyboardButton(text="Ж/Д 🚂", callback_data="railway")
    keyboard.add(button, button2, button3, button4)

    await messsage.answer(text, reply_markup=keyboard)


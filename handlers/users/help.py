from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("@logisticagency_bot — сервис логистических услуг\n\n"
            "<b>Главное</b>\n"
            "/help - показывает это сообщение\n\n"
            "<b>О нас</b>\n"
            "/aboutus — О нас\n"
            "/ouradresses — Наши адреса\n\n"
            "<b>Рассчитать стоимость доставк</b>\n"
            "/bulkorder — Оптовые расчёт\n\n"
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

    await message.answer(text)

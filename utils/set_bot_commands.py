from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Для начала бота"),
            types.BotCommand("help", "Поможет если что то вам не понятно"),
            types.BotCommand("/aboutus", "О нас"),
            types.BotCommand("/ouradresses", "Наши адреса"),
            types.BotCommand("/bulkorder", "Оптовые расчёт"),
            types.BotCommand("/cargostatus",  "Статус груза"),
            types.BotCommand('/alltrackings' ,'Все номера отслеживания'),
            types.BotCommand('/cargoinsurance', 'Страхование груза'),
            types.BotCommand("/shippingrates", "Тарифы доставки грузов (авиа, авто, морем и Ж/Д)"),
            types.BotCommand("/alltrackings", "Все номера отслеживания")
        ]
    )

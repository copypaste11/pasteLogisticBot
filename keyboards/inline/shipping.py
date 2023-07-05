from aiogram import types

from loader import dp, bot

@dp.callback_query_handler(lambda query: query.data == 'sea')
async def handle_sea_button(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("<b>Тарифы доставки морем</b>\n\n"
                                        "- Целый контейнер\n"
                                        "<b>от 0.7$ за кг</b>\n"
                                        "30 - 45 дней\n"
                                        "Страховка 1%\n\n"
                                        "- от 300 кг\n"
                                        "<b>от 1$ за кг</b>\n"
                                        "45 - 60 дней\n"
                                        "Страховка 1,5.%\n\n"
                                        "- от 1000 кг\n"
                                        "<b>от 1$ за кг</b>\n"
                                        "35 - 45 дней\n"
                                        "Страховка 1%")
    

@dp.callback_query_handler(lambda query: query.data == 'air')
async def handle_air_button(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("<b>Тарифы доставки Авиа</b>\n\n"
                                        "- Авиа 'Экспресс' - Кому срочно нужно доставить образцы\n"
                                        "от 50 $ за кг\n"
                                        "<b>от 1 Кг</b>\n"
                                        "2 - 3 дня\n"
                                        "Страховка 3%\n\n"
                                        "- Авиа 'Посылка' - Доставка до вашего города\n"
                                        "120$\n"
                                        "<b>от 1 - 5 Кг</b>\n"
                                        "9 - 14 дня\n"
                                        "Страховка 3%\n\n"
                                        "- Авиа 'Стандарт' - Доставка в Ташкент\n"
                                        "от 7 $ за кг\n"
                                        "<b>от 10 Кг</b>\n"
                                        "9 - 14 дня\n"
                                        "Страховка 2%")
    
@dp.callback_query_handler(lambda query: query.data == 'road')
async def handle_road_button(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("<b>Тарифы доставки авто</b>\n\n"
                                        "- Целый контейнер\n"
                                        "<b>от 0.7$ за кг</b>\n"
                                        "30 - 45 дней\n"
                                        "Страховка 1%\n\n"
                                        "- от 300 кг\n"
                                        "<b>от 1$ за кг</b>\n"
                                        "45 - 60 дней\n"
                                        "Страховка 1,5.%\n\n"
                                        "- от 2 кг\n"
                                        "<b>от 10$ за кг</b>\n"
                                        "45 - 60 дней\n"
                                        "Страховка 1,5.%")
    
@dp.callback_query_handler(lambda query: query.data == 'railway')
async def handle_railway_button(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("<b>Тарифы доставки Ж/Д</b>\n\n"
                                        "- Целый контейнер\n"
                                        "<b>от 0.7$ за кг</b>\n"
                                        "30 - 45 дней\n"
                                        "Страховка 1%\n\n"
                                        "- от 300 кг\n"
                                        "<b>от 1$ за кг</b>\n"
                                        "45 - 60 дней\n"
                                        "Страховка 1,5.%\n\n"
                                        "- от 1000 кг\n"
                                        "от 1$ за кг\n"
                                        "35 - 45 дней\n"
                                        "Страховка 1%")
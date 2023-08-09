
@dp.message_handler(commands=['start'])
async def echo(message: types.message):
    print('бот получил сообщение', message)
    await bot.send_message(CHAT_ID, 'Это @dp.message_handler')
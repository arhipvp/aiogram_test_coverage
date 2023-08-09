from aiogram import Bot, Dispatcher, types
import my_bot



# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я эхо-бот. Просто отправь мне сообщение, и я повторю его.")

# Эхо-обработчик для всех сообщений
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

# Запускаем бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

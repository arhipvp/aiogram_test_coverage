import pytest
from aiogram import Bot, types
from aiogram.utils import exceptions
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


# Фикстура для запуска цикла событий asyncio внутри теста
@pytest.fixture(scope='function')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

# Фикстура для создания инстанса бота, который будет использоваться в тестах
@pytest.fixture(scope='module')
def bot():
    # Здесь необходимо указать токен вашего бота
    bot = Bot(token=TOKEN)
    return bot

# Пример теста, который отправляет сообщение и проверяет, что бот его успешно обработал
@pytest.mark.asyncio
async def test_send_message(bot):
    chat_id = CHAT_ID  # Замените на действительный ID чата
    message_text = "Привет, мир! Это тестовое сообщение от бота."

    try:
        await bot.send_message(chat_id, message_text)
        assert True  # Успешно отправлено
    except exceptions.BotBlocked:
        pytest.fail("Бот заблокирован пользователем")
    except exceptions.ChatNotFound:
        pytest.fail("Чат не найден")
    except exceptions.RetryAfter as e:
        pytest.fail(f"Попробуйте снова через {e.timeout} секунд")
    except exceptions.UserDeactivated:
        pytest.fail("Пользователь деактивирован")
    except exceptions.ChatNotModified:
        pytest.fail("Чат не модифицирован")

if __name__ == '__main__':
    pytest.main()

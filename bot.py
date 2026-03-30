import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

# функция отправки старт-сообщения
async def send_start(message: types.Message):
    name = message.from_user.first_name or "друг"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="🎮 Go",
            web_app=WebAppInfo(url="https://твой-сайт.com")
        )
    )

    await message.answer(
        f"""👋 Привет, {name}!

Нажми на кнопку ниже, чтобы испытать удачу и выиграть редкие подарки Telegram

/terms - условия использования""",
        reply_markup=keyboard
    )

# /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await send_start(message)

# /terms
@dp.message_handler(commands=['terms'])
async def terms(message: types.Message):

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="📄 Политика конфиденциальности",
            url="https://твой-сайт.com/privacy"
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text="📄 Условия использования",
            url="https://твой-сайт.com/terms"
        )
    )

    await message.answer(
        "Ознакомьтесь с условиями использования нашего приложения прежде чем продолжить.",
        reply_markup=keyboard
    )

# ЛОВИТ ТОЛЬКО НЕ команды
@dp.message_handler(lambda message: not message.text.startswith('/'))
async def all_messages(message: types.Message):
    await send_start(message)

if __name__ == "__main__":
    print("Бот запущен 🚀")
    executor.start_polling(dp, skip_updates=True)

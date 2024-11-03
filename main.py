
import logging
from random import choice
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values

# Инициализация бота и диспетчера
token = dotenv_values(".env")["TOKEN"]
bot = Bot(token="7548439593:AAGTiaIPfRJtfK3IgD3Ja80G66hNZlpnU1c")
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет {message.from_user.first_name}")


@dp.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    await message.answer(
        f"ID: {message.from_user.id}\nИмя: Санжар{message.from_user.first_name}\nИмя пользователя:@luntik08_bot {message.from_user.username}"
    )

@dp.message(Command("random"))
async def random_name_handler(message: types.Message):
    name = ["Бекзат @Mandarin4ikpromax", "Абдурахим @TaekoOnukiii", "Тилек @Volverstn", "Гульсана @gullls_s"]
    name = choice(name)
    await message.answer(f"Случайное имя: {name}")


async def main():
    # Запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    import asyncio

    asyncio.run(main())



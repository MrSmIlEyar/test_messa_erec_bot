import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, Contact, WebAppInfo
from aiogram.utils.markdown import hbold
import markup
import config

TOKEN = config.TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(text="Отправить номер 📞", request_contact=True)]
    ])
    await message.answer("Для регистрации необходимо отправить номер телефона, нажав на соответствующую кнопку ниже", reply_markup=keyboard)



@dp.message()
async def handle_contact(message: types.ContentType.CONTACT):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(text="Открыть веб-приложение", web_app=WebAppInfo(url="https://lichess.org/"))]
    ])
    contact = message.contact
    await message.answer(f"Вы успешно зарегистрировались! \nВаш номер телефона: {contact.phone_number}", reply_markup=keyboard)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

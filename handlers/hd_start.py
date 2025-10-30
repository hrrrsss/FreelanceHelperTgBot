from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from common.connect_text import WELCOME_TEXT
from keyboards.start_kb import start_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(WELCOME_TEXT, 
                         disable_web_page_preview=True, 
                         reply_markup=start_keyboard)
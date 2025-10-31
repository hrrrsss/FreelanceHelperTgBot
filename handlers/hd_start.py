from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from common.connect_text import WELCOME_TEXT
from keyboards.basic_kb import kb_builder
from common.connect_profile import start_profile


start_router = Router()


@start_router.message(CommandStart())
async def start_cmd(message: Message):
    start_profile(message.from_user.id)
    await message.answer(WELCOME_TEXT, 
                         disable_web_page_preview=True, 
                         reply_markup=kb_builder.as_markup())
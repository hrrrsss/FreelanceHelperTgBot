from aiogram import Router, F
from aiogram.types import CallbackQuery


basic_router = Router()


@basic_router.callback_query(F.data == 'button2_click')
async def profile(callback: CallbackQuery):
    await callback.answer()
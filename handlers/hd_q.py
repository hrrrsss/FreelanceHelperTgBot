from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from datetime import datetime, timedelta

from common.fsm_q_cmd import load_last_requests, save_last_requests
from common.connect_text import ADMIN_ID


q_router = Router()


last_request_time = load_last_requests()


class QForm(StatesGroup):
    waiting_for_message = State()


@q_router.message(Command("q"))
async def q_cmd(message: Message, state: FSMContext):
    user_id = message.from_user.id
    now = datetime.now()

    if user_id in last_request_time and now - last_request_time[user_id] < timedelta(days=1):
        await message.answer("⏳ Вы уже отправляли запрос сегодня. Попробуйте снова завтра.")
        return
    
    await message.answer("✉️ Опишите вашу проблему, ошибку или предложение (только текстом):")
    await state.set_state(QForm.waiting_for_message)


@q_router.message(QForm.waiting_for_message, F.text)
async def process_q_text(message: Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text

    await message.bot.send_message(
        ADMIN_ID,
        f"Новое сообщение от @{message.from_user.username or 'без_ника'} (ID: {user_id}):\n\n{text}"
    )

    await message.answer("✅ Ваше сообщение отправлено! Спасибо за обратную связь.")

    last_request_time[user_id] = datetime.now()
    save_last_requests(last_request_time)

    await state.clear()


@q_router.message(QForm.waiting_for_message)
async def process_non_text(message: Message):
    await message.answer("⚠️ Пожалуйста, отправьте текстовое сообщение без вложений.")
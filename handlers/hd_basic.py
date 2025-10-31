from aiogram import Router, F
from aiogram.types import CallbackQuery

from common.connect_text import PROFILE_TEXT, WELCOME_TEXT, TARIFS_TEXT
from common.connect_profile import read_profile, change_profile
from keyboards.basic_kb import kb_builder2, kb_builder, kb_builder3


basic_router = Router()


@basic_router.callback_query(F.data == 'button2_click')
async def profile(callback: CallbackQuery):
    await callback.message.edit_text(
        text=PROFILE_TEXT.format(name=callback.from_user.full_name,
                                 tarif=read_profile(callback.from_user.id)[0],
                                 time=read_profile(callback.from_user.id)[1],
                                 all_filters=read_profile(callback.from_user.id)[2]),
        reply_markup=kb_builder2.as_markup()
    )


@basic_router.callback_query(F.data == 'button3_click')
async def tarifs(callback: CallbackQuery):
    await callback.message.edit_text(
        text=TARIFS_TEXT,
        reply_markup=kb_builder3.as_markup()
    )


@basic_router.callback_query(F.data == 'button4_click')
async def home(callback: CallbackQuery):
    await callback.message.edit_text(
                         WELCOME_TEXT, 
                         disable_web_page_preview=True, 
                         reply_markup=kb_builder.as_markup()

    )


@basic_router.callback_query(F.data.in_(["button5_click", "button6_click"]))
async def tarif_plus(callback: CallbackQuery):
    change_profile(callback.from_user.id, callback.data)
    tarif = read_profile(callback.from_user.id)[0]
    await callback.answer(text=f'Сделаем вид, что вы оплатали\nВаша тариф теперь - {tarif}', show_alert=True)


@basic_router.callback_query(F.data == 'button7_click')
async def date_more(callback: CallbackQuery):
    change_profile(callback.from_user.id, callback.data)
    await callback.answer(text='Сделаем вид, что вы оплитили\nТеперь тариф доступен на полгода', show_alert=True)
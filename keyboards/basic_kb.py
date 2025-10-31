from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


kb_builder = InlineKeyboardBuilder()
buttons1 = [InlineKeyboardButton(text='Категории', callback_data='button1_click'),
            InlineKeyboardButton(text='👤Профиль', callback_data='button2_click')]
kb_builder.row(*buttons1)


kb_builder2 = InlineKeyboardBuilder()
buttons2 = [InlineKeyboardButton(text='💸Тарифы', callback_data='button3_click'),
            InlineKeyboardButton(text='🏠В начало', callback_data='button4_click')]
kb_builder2.row(*buttons2)


kb_builder3 = InlineKeyboardBuilder()
buttons3 = [InlineKeyboardButton(text='🔸Plus — 100 ₽ (мес.)', callback_data='button5_click'),
            InlineKeyboardButton(text='🔥Pro — 500 ₽ (мес.)', callback_data='button6_click'),
            InlineKeyboardButton(text='💸Купить больше месяца', callback_data='button7_click'),
            InlineKeyboardButton(text='🏠В начало', callback_data='button4_click'),
            InlineKeyboardButton(text='👤Профиль', callback_data='button2_click')]
kb_builder3.add(*buttons3)
kb_builder3.adjust(1, 1, 1, 2)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_1 = InlineKeyboardButton(text='Категории', callback_data='button1_click')
button_2 = InlineKeyboardButton(text='Профиль', callback_data='button2_click')


start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_1], [button_2]])
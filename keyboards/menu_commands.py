from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from common.connect_text import MENU_TEXT


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=command, description=description)
        for command, description in MENU_TEXT.items()
    ]
    await bot.set_my_commands(
        commands=main_menu_commands,
        scope=BotCommandScopeAllPrivateChats()
    )
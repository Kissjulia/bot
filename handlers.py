from aiogram import types, Dispatcher


import commands

def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_bot, commands=['start', 'bot_up'])
    dp.register_message_handler(commands.move_player)
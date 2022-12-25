from config import dp, bot
from aiogram import types

total = 150

@dp.message_handler(commands=['start', 'next_move'])
async def start_bot(message: types.Message):
    print(message.text)


@dp.message_handler()
async def all_bot(message: types.Message):
    global total
    take = int(message.text)
    if 0 < take < 29:
        total -= int(message.text)
        await message.reply(f'{message.from_user.first_name},'
                                                 f'ты взяла {message.text} конфет, и на столе осталось {total} конфет')
    else:
        await message.reply(f'Ах ты хитрая, {message.from_user.first_name}, не жульничай')


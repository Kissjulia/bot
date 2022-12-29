from config import dp, bot
from aiogram import types
from random import randint
total = 150

@dp.message_handler(commands=['start', 'next_move'])
async def start_bot(message: types.Message):
    print(message.text)


@dp.message_handler()
async def move_player(message: types.Message):
    global total
    take = int(message.text)
    if 0 < take < 29:
        total -= int(message.text)
        await message.reply(f'{message.from_user.first_name},'
                                                 f'ты взяла {message.text} конфет, и на столе осталось {total} конфет')
    else:
        await message.reply(f'Ах ты хитрая, {message.from_user.first_name}, не жульничай')


@dp.message_handler()
def move_bot(candies, max_move):
    move = randint(1, max_move) if candies >= max_move else randint(1, candies)
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies

@dp.message_handler()
def check_win(candies, determing_moves, first_name, second_name):
    if candies == 0:
        return first_name if determing_moves % 2 == 0 else second_name
    else:
        return False


@dp.message_handler()
def player_vs_bot(message: types.Message):
        candies = 150
        max_move = 28
        count_for_check_win = candies // max_move
        determing_moves = randint(0, 1)
        win = False
        while not win:
            if determing_moves % 2 == 0:
                candies = move_player(message.from_user.first_name, candies, max_move)
            else:
                candies = move_bot(candies, max_move)
            if determing_moves >= count_for_check_win - 1:
                temp = check_win(candies, determing_moves, message.from_user.first_name, 'Бот')
                if temp:
                    print(f'{temp} выиграл')
                    win = True
            determing_moves += 1
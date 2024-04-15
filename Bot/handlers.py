from aiogram import types, F
from aiogram.filters.command import Command
from loader import dp
from keyboards import menu_keyboard


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("---", reply_markup=menu_keyboard)


@dp.message(Command('kubik'))
async def dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@dp.message(F.text)
async def echo(message: types.Message):
    await message.reply(message.text)

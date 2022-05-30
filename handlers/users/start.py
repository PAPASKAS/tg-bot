import aiogram.utils.exceptions
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncio
import csv

from loader import dp, bot
from data.config import Messages, Buttons, Codes, Videos, ADMINS
from states.states import VideosState


yes_no_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
yes_no_menu.add(KeyboardButton(Buttons.yes))
yes_no_menu.add(KeyboardButton(Buttons.no))

timing: int = 10


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state()

    await message.answer(Messages.greetings, reply_markup=yes_no_menu)
    await VideosState.first_video.set()


@dp.message_handler(lambda message: message.text.lower() in (Buttons.yes.lower(), Buttons.no.lower()), state=VideosState.first_video)
async def first_video(message: types.Message, state):
    if message.text == Buttons.no:
        await message.answer(Messages.reject)
        await state.finish()
        return

    await message.answer(Messages.start_watching, reply_markup=None)

    await bot.send_video(message.chat.id, Videos.first)

    await asyncio.sleep(Videos.first_length - timing)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(Codes.first))
    await message.answer(Messages.write_code, reply_markup=keyboard)
    await VideosState.next()


@dp.message_handler(lambda message: message.text == Codes.first, state=VideosState.second_video)
async def second_video(message: types.Message, state):
    await message.answer(Messages.first_answer)
    await bot.send_video(message.chat.id, Videos.second)

    await asyncio.sleep(Videos.second_length - timing)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(Codes.second))
    await message.answer(Messages.write_code, reply_markup=keyboard)
    await VideosState.next()


@dp.message_handler(lambda message: message.text == Codes.second, state=VideosState.third_video)
async def third_video(message: types.Message, state):
    await message.answer(Messages.second_answer)
    await bot.send_video(message.chat.id, Videos.third)

    await asyncio.sleep(Videos.third_length - timing)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(Codes.third))
    await message.answer(Messages.write_code, reply_markup=keyboard)
    await VideosState.next()


@dp.message_handler(lambda message: message.text == Codes.third, state=VideosState.fourth_video)
async def third_video(message: types.Message, state):
    await message.answer(Messages.third_answer)
    await bot.send_video(message.chat.id, Videos.fourth)

    await asyncio.sleep(Videos.fourth_length - timing)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton(Codes.fourth))
    await message.answer(Messages.write_code, reply_markup=keyboard)
    await VideosState.next()


@dp.message_handler(lambda message: message.text == Codes.fourth, state=VideosState.fifth_video)
async def third_video(message: types.Message, state):
    await message.answer(Messages.fourth_answer)
    await bot.send_video(message.chat.id, Videos.fifth)

    await asyncio.sleep(Videos.fifth_length - timing)
    await message.answer(Messages.fifths_answer)
    await bot.send_video(message.chat.id, Videos.sixth)
    await asyncio.sleep(Videos.sixth_length - timing)
    await message.answer(Messages.sixth_answer)

    with open('volumes/finishUsers.csv', 'a', newline='') as csvfile:
        spam_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spam_writer.writerow([message.from_user.id, message.from_user.full_name, message.from_user.username])

    await state.finish()


@dp.message_handler(commands=['admin'], user_id=ADMINS)
async def admin(message: types.Message, state):
    msg = message.text[7:]  # delete from str - /admin

    with open('volumes/finishUsers.csv', 'r', newline='') as csvfile:
        spam_reader = csv.reader(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        users_id = []
        for row in spam_reader:
            users_id.append(int(row[0]))

        unique_users_id = set(users_id)
        for user_id in unique_users_id:
            try:
                await bot.send_message(user_id, msg)
            except aiogram.utils.exceptions.ChatNotFound:
                continue


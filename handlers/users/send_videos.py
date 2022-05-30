from aiogram import types

from loader import dp
from data.config import ADMINS


@dp.message_handler(content_types=["video"], state='*', user_id=ADMINS)
async def bot_start(message: types.Message):
    await message.answer(message.video.file_id)


#!/usr/bin/env python3.9

from aiogram import executor
import asyncio

from loader import dp
import middlewares, handlers
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await asyncio.sleep(1)
    await set_default_commands(dispatcher)
    print("Bot started")


async def on_shutdown(dispatcher):
    print("Bot stopped")
    dispatcher.stop_polling()
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)

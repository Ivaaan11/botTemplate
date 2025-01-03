from app.handlers import user, admin, payments
from app.database.models import async_main
import app.middlewares as middlewares

import asyncio
import logging
import os

from dotenv import load_dotenv

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand, BotCommandScopeDefault



commands = [
    BotCommand(command = 'start', description = 'Starts the bot'),
]


async def main():
    await async_main()
    load_dotenv()

    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()

    # dp.update.middleware(middleware)
    dp.message.middleware(middlewares.CancelMiddleware())
    dp.include_routers(
        user.router,
        admin.router,
        payments.router
    )
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

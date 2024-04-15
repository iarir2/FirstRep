import logging
import asyncio

from loader import dp, bot
from aiogram import Dispatcher
import handlers


async def on_startup(dispatcher: Dispatcher) -> None:
    pass

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    asyncio.run(main())

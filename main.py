import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from config import Config, load_config

logger = logging.getLogger(__name__)


async def main():
    config: Config = load_config()

    logging.basicConfig(
        level = logging.getLevelName(level=config.log.level),
        format=config.log.format
    )


    logger.info('Starting bot...')
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    # Skip old updates and run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

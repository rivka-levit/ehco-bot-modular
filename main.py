import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from config import Config, load_config
from handlers import other, user

logger = logging.getLogger(__name__)


async def main():
    config: Config = load_config()

    logging.basicConfig(
        level = logging.getLevelName(level=config.log.level),
        format=config.log.format,
        stream=sys.stdout
    )


    logger.info('Starting bot...')

    # Create bot instance
    bot = Bot(token=config.bot.token)

    # Create main router and register other routers
    dp = Dispatcher()
    dp.include_router(user.router)
    dp.include_router(other.router)

    # Skip old updates and run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

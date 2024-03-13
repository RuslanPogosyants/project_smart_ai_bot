import asyncio
import logging
from aiogram import Bot, Dispatcher
from dependencies import telegram_token
from handlers import register_client_handlers
from config import bot, dp

logging.basicConfig(level=logging.INFO)


# Запуск процесса поллинга новых апдейтов
async def main():
    register_client_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

from aiogram import Dispatcher, types
from aiogram import F
from ai_api.text_generator import request_answer
from ai_api.img_generator import request_img_answer
from aiogram.filters import Command
from config import bot
from aiogram.types.input_file import BufferedInputFile


async def get_text_answer(message: types.Message):
    question = message.text
    await message.answer(request_answer(question))


async def get_img_answer(message: types.Message):
    question = message.text
    image_bytes = request_img_answer(question)
    text_file = BufferedInputFile(file=image_bytes, filename="file.txt")
    await bot.send_photo(message.chat.id, photo=text_file)


def register_client_handlers(dp: Dispatcher):
    dp.message.register(get_text_answer, F.text.startswith('/str'))
    dp.message.register(get_img_answer, F.text.startwith('/img'))

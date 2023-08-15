from aiogram import Router
from aiogram.types import Message
from aiogram import Bot
import config

router = Router()
bot = Bot(token=config.BOT_TOKEN)

stickers = ['cockstick']
exception = 'AgAD8hkAAkFkyUo'

@router.message()
async def message_handler(msg: Message):
    for word in stickers:
        if msg.sticker:
            print(msg.sticker.file_unique_id)
            if word == msg.sticker.set_name and exception != msg.sticker.file_unique_id:
                await msg.answer(f"{msg.from_user.first_name}, ты один посмотрел на голый ХУЙ")
                await bot.delete_message(msg.chat.id, msg.message_id)
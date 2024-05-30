from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.core.call import Anony

hosgeldiniz = 20
kapat = 30

@app.on_message(filters.video_chat_started, group=hosgeldiniz)
@app.on_message(filters.video_chat_ended, group=kapat)
async def hosgeldiniz(_, message: Message):
    await Anony.stop_stream_force(message.chat.id)

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    baslangic = datetime.now()
    yanit_foto = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytg_pingu = await Anony.ping()
    ÇALIŞMA, CPU, RAM, DİSK = await bot_sys_stats()
    yanit_suresi = (datetime.now() - baslangic).microseconds / 1000
    await yanit_foto.edit_text(
        _["ping_2"].format(yanit_suresi, app.mention, ÇALIŞMA, RAM, CPU, DİSK, pytg_pingu),
        reply_markup=supp_markup(_),
    )
    

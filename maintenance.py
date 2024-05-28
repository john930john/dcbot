from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import (
    get_lang,
    is_maintenance,
    maintenance_off,
    maintenance_on,
)
from strings import get_string


@app.on_message(filters.command(["bakım"]) & SUDOERS)
async def bakim(client, message: Message):
    try:
        dil = await get_lang(message.chat.id)
        _ = get_string(dil)
    except:
        _ = get_string("tr")  # Varsayılan olarak Türkçe dil kullanılacak
    kullanım = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(kullanım)
    durum = message.text.split(None, 1)[1].strip().lower()
    if durum == "etkinleştir":
        if await is_maintenance() is False:
            await message.reply_text(_["maint_4"])
        else:
            await maintenance_on()
            await message.reply_text(_["maint_2"].format(app.mention))
    elif durum == "devre dışı":
        if await is_maintenance() is False:
            await maintenance_off()
            await message.reply_text(_["maint_3"].format(app.mention))
        else:
            await message.reply_text(_["maint_5"])
    else:
        await message.reply_text(kullanım)

from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.utils.database import get_loop, set_loop
from AnonXMusic.utils.decorators import AdminRightsCheck
from AnonXMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["loop", "cloop", "tekrarla"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def admins(cli, message: Message, _, chat_id):
    kullanım = _["admin_17"]
    if len(message.command) != 2:
        return await message.reply_text(kullanım)
    durum = message.text.split(None, 1)[1].strip()
    if durum.isnumeric():
        durum = int(durum)
        if 1 <= durum <= 10:
            var = await get_loop(chat_id)
            if var != 0:
                durum = var + durum
            if int(durum) > 10:
                durum = 10
            await set_loop(chat_id, durum)
            return await message.reply_text(
                text=_["admin_18"].format(durum, message.from_user.mention),
                reply_markup=close_markup(_),
            )
        else:
            return await message.reply_text(_["admin_17"])
    elif durum.lower() == "etkinleştir":
        await set_loop(chat_id, 10)
        return await message.reply_text(
            text=_["admin_18"].format(durum, message.from_user.mention),
            reply_markup=close_markup(_),
        )
    elif durum.lower() == "devre dışı":
        await set_loop(chat_id, 0)
        return await message.reply_text(
            _["admin_19"].format(message.from_user.mention),
            reply_markup=close_markup(_),
        )
    else:
        return await message.reply_text(kullanım)
        

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from AnonXMusic import app
from AnonXMusic.utils.database import get_playmode, get_playtype, is_nonadmin_chat
from AnonXMusic.utils.decorators import language
from AnonXMusic.utils.inline.settings import playmode_users_markup
from config import BANNED_USERS


@app.on_message(filters.command(["oynatmamodu", "mod"]) & filters.group & ~BANNED_USERS)
@language
async def oynatma_modu(client, message: Message, _):
    oynatma_modu = await get_playmode(message.chat.id)
    if oynatma_modu == "Doğrudan":
        Dogrudan = True
    else:
        Dogrudan = None
    yonetici_degil_mi = await is_nonadmin_chat(message.chat.id)
    if not yonetici_degil_mi:
        Grup = True
    else:
        Grup = None
    oynatma_tipi = await get_playtype(message.chat.id)
    if oynatma_tipi == "Herkes":
        Oynatmatipi = None
    else:
        Oynatmatipi = True
    butonlar = playmode_users_markup(_, Dogrudan, Grup, Oynatmatipi)
    yanit = await message.reply_text(
        _["oynat_22"].format(message.chat.title),
        reply_markup=InlineKeyboardMarkup(butonlar),
    )
    

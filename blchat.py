from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import blacklist_chat, blacklisted_chats, whitelist_chat
from AnonXMusic.utils.decorators.language import language
from config import BANNED_USERS

@app.on_message(filters.command(["siyahliste", "sohbetekle"]) & SUDOERS)
@language
async def siyah_liste_ekle(client, message: Message, _):
    if len(message.command) != 2:
        return await message.reply_text(_["siyah_1"])
    sohbet_id = int(message.text.strip().split()[1])
    if sohbet_id in await blacklisted_chats():
        return await message.reply_text(_["siyah_2"])
    siyah_listeye_eklendi = await blacklist_chat(sohbet_id)
    if siyah_listeye_eklendi:
        await message.reply_text(_["siyah_3"])
    else:
        await message.reply_text(_["siyah_9"])
    try:
        await app.leave_chat(sohbet_id)
    except:
        pass

@app.on_message(
    filters.command(["beyazliste", "siyahlistedengelcıkar", "siyahlistedencıkar"]) & SUDOERS
)
@language
async def beyaz_liste(client, message: Message, _):
    if len(message.command) != 2:
        return await message.reply_text(_["siyah_4"])
    sohbet_id = int(message.text.strip().split()[1])
    if sohbet_id not in await blacklisted_chats():
        return await message.reply_text(_["siyah_5"])
    beyaz_listeye_eklendi = await whitelist_chat(sohbet_id)
    if beyaz_listeye_eklendi:
        return await message.reply_text(_["siyah_6"])
    await message.reply_text(_["siyah_9"])

@app.on_message(filters.command(["siyahlisteler", "siyahlistedensohbetler"]) & ~BANNED_USERS)
@language
async def tum_sohbetler(client, message: Message, _):
    text = _["siyah_7"]
    j = 0
    for say, sohbet_id in enumerate(await blacklisted_chats(), 1):
        try:
            baslik = (await app.get_chat(sohbet_id)).title
        except:
            baslik = "Özel Sohbet"
        j = 1
        text += f"{say}. {baslik}[<code>{sohbet_id}</code>]\n"
    if j == 0:
        await message.reply_text(_["siyah_8"].format(app.mention))
    else:
        await message.reply_text(text)
        

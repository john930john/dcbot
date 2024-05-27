from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)

@app.on_message(filters.command(["aktifvc", "aktifsese"]))  # SUDOERS ekleyebilirsiniz
async def aktifvc(_, message: Message):
    mystic = await message.reply_text("» Aktif sesli sohbetler listeleniyor...")
    aktif_sohbetler = await get_active_chats()
    metin = ""
    j = 0
    for x in aktif_sohbetler:
        try:
            baslik = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                kullanici = (await app.get_chat(x)).username
                metin += f"<b>{j + 1}.</b> <a href=https://t.me/{kullanici}>{unidecode(baslik).upper()}</a> [<code>{x}</code>]\n"
            else:
                metin += (
                    f"<b>{j + 1}.</b> {unidecode(baslik).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not metin:
        await mystic.edit_text(f"» {app.mention} üzerinde aktif sesli sohbet bulunmuyor.")
    else:
        await mystic.edit_text(
            f"<b>» Şu anda aktif olan sesli sohbetler :</b>\n\n{metin}",
            disable_web_page_preview=True,
        )

@app.on_message(filters.command(["aktifv", "aktifvideo"]))  # SUDOERS ekleyebilirsiniz
async def aktifv(_, message: Message):
    mystic = await message.reply_text("» Aktif video sohbetler listeleniyor...")
    aktif_video_sohbetler = await get_active_video_chats()
    metin = ""
    j = 0
    for x in aktif_video_sohbetler:
        try:
            baslik = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                kullanici = (await app.get_chat(x)).username
                metin += f"<b>{j + 1}.</b> <a href=https://t.me/{kullanici}>{unidecode(baslik).upper()}</a> [<code>{x}</code>]\n"
            else:
                metin += (
                    f"<b>{j + 1}.</b> {unidecode(baslik).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not metin:
        await mystic.edit_text(f"» {app.mention} üzerinde aktif video sohbet bulunmuyor.")
    else:
        await mystic.edit_text(
            f"<b>» Şu anda aktif olan video sohbetler :</b>\n\n{metin}",
            disable_web_page_preview=True,
            )
                

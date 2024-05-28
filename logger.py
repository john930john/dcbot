from pyrogram.enums import ParseMode

from AnonXMusic import app
from AnonXMusic.utils.database import is_on_off
from config import LOGGER_ID

async def oynatma_kayitlari(mesaj, akis_turu):
    if await is_on_off(2):
        kayitci_metin = f"""
<b>{app.mention} OYNATMA KAYDI</b>

<b>Sohbet ID :</b> <code>{mesaj.chat.id}</code>
<b>Sohbet Adı :</b> {mesaj.chat.title}
<b>Sohbet Kullanıcı Adı :</b> @{mesaj.chat.username}

<b>Kullanıcı ID :</b> <code>{mesaj.from_user.id}</code>
<b>Adı :</b> {mesaj.from_user.mention}
<b>Kullanıcı Adı :</b> @{mesaj.from_user.username}

<b>Sorgu :</b> {mesaj.text.split(None, 1)[1]}
<b>Akış Türü :</b> {akis_turu}"""
        if mesaj.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=kayitci_metin,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
        

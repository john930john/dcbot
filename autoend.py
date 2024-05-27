from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import otomatik_sonlandırma_kapat, otomatik_sonlandırma_ac


@app.on_message(filters.command("otomatiksonlandırma") & SUDOERS)
async def otomatik_sonlandırma_ak_kapat(_, message: Message):
    kullanim = "<b>Örnek:</b>\n\n/otomatiksonlandırma [aç | kapat]"
    if len(message.command) != 2:
        return await message.reply_text(kullanim)
    durum = message.text.split(None, 1)[1].strip().lower()
    if durum == "aç":
        await otomatik_sonlandırma_ac()
        await message.reply_text(
            "» Otomatik sonlandırma özelliği açıldı.\n\nAsistan, kimse dinlemediğinde video sohbeti otomatik olarak terk edecektir."
        )
    elif durum == "kapat":
        await otomatik_sonlandırma_kapat()
        await message.reply_text("» Otomatik sonlandırma özelliği kapatıldı.")
    else:
        await message.reply_text(kullanim)
        

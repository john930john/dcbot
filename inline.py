from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython.__future__ import VideosSearch

from AnonXMusic import app
from AnonXMusic.utils.inlinequery import answer
from config import BANNED_USERS


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    metin = query.query.strip().lower()
    cevaplar = []
    if metin.strip() == "":
        try:
            await client.answer_inline_query(query.id, results=answer, cache_time=10)
        except:
            return
    else:
        arama = VideosSearch(metin, limit=20)
        sonuç = (await arama.next()).get("result")
        for x in range(15):
            başlık = (sonuç[x]["title"]).title()
            süre = sonuç[x]["duration"]
            görüntülenme = sonuç[x]["viewCount"]["short"]
            kapak = sonuç[x]["thumbnails"][0]["url"].split("?")[0]
            kanal_linki = sonuç[x]["channel"]["link"]
            kanal = sonuç[x]["channel"]["name"]
            link = sonuç[x]["link"]
            yayınlanma = sonuç[x]["publishedTime"]
            açıklama = f"{görüntülenme} | {süre} dakika | {kanal}  | {yayınlanma}"
            düğmeler = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="YouTube 🎄",
                            url=link,
                        )
                    ],
                ]
            )
            aranan_metin = f"""
❄ <b>Başlık :</b> <a href={link}>{başlık}</a>

⏳ <b>Süre :</b> {süre} dakika
👀 <b>Görüntülenme :</b> <code>{görüntülenme}</code>
🎥 <b>Kanal :</b> <a href={kanal_linki}>{kanal}</a>
⏰ <b>Yayınlanma :</b> {yayınlanma}


<u><b>➻ Moda Göre Satır İçi Arama {app.name}</b></u>"""
            cevaplar.append(
                InlineQueryResultPhoto(
                    photo_url=kapak,
                    title=başlık,
                    thumb_url=kapak,
                    description=açıklama,
                    caption=aranan_metin,
                    reply_markup=düğmeler,
                )
            )
        try:
            return await client.answer_inline_query(query.id, results=cevaplar)
        except:
            return
            

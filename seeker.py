import asyncio

from AnonXMusic.misc import db
from AnonXMusic.utils.database import get_active_chats, is_music_playing


async def zamanlayıcı():
    while not await asyncio.sleep(1):
        aktif_sohbetler = await get_active_chats()
        for sohbet_id in aktif_sohbetler:
            if not await is_music_playing(sohbet_id):
                continue
            oynatilan = db.get(sohbet_id)
            if not oynatilan:
                continue
            süre = int(oynatilan[0]["seconds"])
            if süre == 0:
                continue
            if db[sohbet_id][0]["played"] >= süre:
                continue
            db[sohbet_id][0]["played"] += 1


asyncio.create_task(zamanlayıcı())

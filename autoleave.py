import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from AnonXMusic import app
from AnonXMusic.core.çağrı import Anony, otomatik_ayrılma
from AnonXMusic.utils.database import get_client, is_active_chat, otomatik_ayrılma_durumu, otomatik_sonlandırma_durumu


async def otomatik_ayrılma():
    if config.OTOMATIK_AYRILMA_ASSİSTANI:
        while not await asyncio.sleep(900):
            from AnonXMusic.core.userbot import asistanlar

            for num in asistanlar:
                client = await get_client(num)
                ayrıldı = 0
                try:
                    async for i in client.get_dialogs():
                        if i.chat.type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                            if (
                                i.chat.id != config.LOGGER_ID
                                and i.chat.id != -1001686672798
                                and i.chat.id != -1001549206010
                            ):
                                if ayrıldı == 20:
                                    continue
                                if not await is_active_chat(i.chat.id):
                                    try:
                                        await client.leave_chat(i.chat.id)
                                        ayrıldı += 1
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(otomatik_ayrılma())


async def otomatik_sonlandırma():
    while not await asyncio.sleep(5):
        sonlandırıcı = await otomatik_sonlandırma_durumu()
        if not sonlandırıcı:
            continue
        for sohbet_id in otomatik_ayrılma:
            zamanlayıcı = otomatik_ayrılma.get(sohbet_id)
            if not zamanlayıcı:
                continue
            if datetime.now() > zamanlayıcı:
                if not await is_active_chat(sohbet_id):
                    otomatik_ayrılma[sohbet_id] = {}
                    continue
                otomatik_ayrılma[sohbet_id] = {}
                try:
                    await An
                    

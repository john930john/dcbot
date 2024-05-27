from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self, dil):
        LOGGER(__name__).info(f"Bot Başlatılıyor...")
        super().__init__(
            name="AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )
        self.dil = dil

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} bot başlatıldı :</b><u>\n\nID : <code>{self.id}</code>\nİsim : {self.name}\nKullanıcı Adı : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot, log grubu/kanalına erişemedi. Lütfen botunuzu log grubu/kanalınıza eklediğinizden emin olun."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot, log grubu/kanalına erişemedi.\n  Sebep: {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Lütfen botunuzu log grubu/kanalında yönetici olarak atayın."
            )
            exit()
        LOGGER(__name__).info(f"Müzik Botu {self.name} olarak başlatıldı")

    async def stop(self):
        await super().stop()
        

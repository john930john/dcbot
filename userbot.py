from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AnonXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="AnonXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="AnonXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="AnonXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="AnonXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("sorundestekk")
                await self.one.join_chat("esilabotbilgilendirme")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("DevilsHeavenMF")
                await self.two.join_chat("FallenAssociation")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("DevilsHeavenMF")
                await self.three.join_chat("FallenAssociation")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("DevilsHeavenMF")
                await self.four.join_chat("FallenAssociation")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("DevilsHeavenMF")
                await self.five.join_chat("FallenAssociation")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
ChatGPT
It seems like you're creating multiple instances of the Pyrogram Client class for different assistant accounts. Each instance corresponds to a different assistant account with its own session string. Then, you're starting these assistants and joining them to specific chat groups.



from pyrogram import Client

import config

from ..logging import LOGGER

yardımcılar = []
yardımcı_idler = []


class KullanıcıBotu(Client):
    def __init__(self):
        self.bir = Client(
            ad="AnonXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            oturum_dizesi=str(config.STRING1),
            güncellemeleri_yok=True,
        )
        self.iki = Client(
            ad="AnonXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            oturum_dizesi=str(config.STRING2),
            güncellemeleri_yok=True,
        )
        self.üç = Client(
            ad="AnonXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            oturum_dizesi=str(config.STRING3),
            güncellemeleri_yok=True,
        )
        self.dört = Client(
            ad="AnonXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            oturum_dizesi=str(config.STRING4),
            güncellemeleri_yok=True,
        )
        self.beş = Client(
            ad="AnonXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            oturum_dizesi=str(config.STRING5),
            güncellemeleri_yok=True,
        )

    async def başlat(self):
        LOGGER(__name__).info(f"Yardımcılar başlatılıyor...")
        if config.STRING1:
            await self.bir.start()
            try:
                await self.bir.join_chat("sorundestekk")
                await self.bir.join_chat("esilabotbilgilendirme")
            except:
                pass
            yardımcılar.append(1)
            try:
                await self.bir.send_message(config.LOGGER_ID, "Yardımcı başlatıldı")
            except:
                LOGGER(__name__).error(
                    "Yardımcı Hesap 1, log Grubuna erişemedi. Yardımcınızı log grubunuza eklediğinizden ve yönetici olarak tanıttığınızdan emin olun!"
                )
                exit()
            self.bir.id = self.bir.me.id
            self.bir.ad = self.bir.me.mention
            self.bir.kullanıcı_adı = self.bir.me.username
            yardımcı_idler.append(self.bir.id)
            LOGGER(__name__).info(f"{self.bir.ad} olarak Yardımcı Başlatıldı")

        if config.STRING2:
            await self.iki.start()
            try:
                await self.iki.join_chat("DevilsHeavenMF")
                await self.iki.join_chat("FallenAssociation")
            except:
                pass
            yardımcılar.append(2)
            try:
                await self.iki.send_message(config.LOGGER_ID, "Yardımcı başlatıldı")
            except:
                LOGGER(__name__).error(
                    "Yardımcı Hesap 2, log Grubuna erişemedi. Yardımcınızı log grubunuza eklediğinizden ve yönetici olarak tanıttığınızdan emin olun!"
                )
                exit()
            self.iki.id = self.iki.me.id
            self.iki.ad = self.iki.me.mention
            self.iki.kullanıcı_adı = self.iki.me.username
            yardımcı_idler.append(self.iki.id)
            LOGGER(__name__).info(f"{self.iki.ad} olarak Yardımcı Başlatıldı")

        if config.STRING3:
            await self.üç.start()
            try:
                await self.üç.join_chat("DevilsHeavenMF")
                await self.üç.join_chat("FallenAssociation")
            except:
                pass
            yardımcılar.append(3)
            try:
                await self.üç.send_message(config.LOGGER_ID, "Yardımcı başlatıldı")
            except:
                LOGGER(__name__).error(
                    "Yardımcı Hesap 3, log Grubuna erişemedi. Yardımcınızı log grubunuza eklediğinizden ve yönetici olarak tanıttığınızdan emin olun!"
                )
                exit()
            self.üç.id = self.üç.me.id
            self.üç.ad = self.üç.me.mention
            self.üç.kullanıcı_adı = self.üç.me.username
            yardımcı_idler.append(self.üç.id)
            LOGGER(__name__).info(f"{self.üç.ad} olarak Yardımcı Başlatıldı")

        if config.STRING4:
            await self.dört.start()
            try:
                await self.dört.join_chat("DevilsHeavenMF")
                await self.dört.join_chat("FallenAssociation")
            except:
                pass
            yardımcılar.append(4)
            try:
                await self.dört.send_message(config.LOGGER_ID, "Yardımcı başlatıldı")
            except:
                LOGGER(__name__).error(
                    "Yardımcı Hesap 4, log Grubuna erişemedi. Yardımcınızı log grubunuza eklediğinizden ve yönetici olarak tanıttığınızdan emin olun!"
                )
                exit()
            self.dört.id = self.dört.me.id
            self.dört.ad = self.dört.me.mention
            self.dört.kullanıcı_adı = self.dört.me.username
            yardımcı_idler.append(self.dört.id)
            LOGGER(__name__).info(f"{self.dört.ad} olarak Yardımcı Başlatıldı")

        if config.STRING5:
            await self.beş.start()
            try:
                await self.beş.join_chat("DevilsHeavenMF")
                await self.beş.join_chat("FallenAssociation")
            except:
                pass
            yardımcılar.append(5)
            try:
                await self.beş.send_message(config.LOGGER_ID, "Yardımcı başlatıldı")
            except:
                LOGGER(__name__).error(
                    "Yardımcı Hesap 5, log Grubuna erişemedi. Yardımcınızı log grubunuza eklediğinizden ve yönetici olarak tanıttığınızdan emin olun!"
                )
                exit()
            self.beş.id = self.beş.me.id
            self.beş.ad = self.beş.me.mention
            self.beş.kullanıcı_adı = self.beş.me.username
            yardımcı_idler.append(self.beş.id)
            LOGGER(__name__).info(f"{self.beş.ad} olarak Yardımcı Başlatıldı")

    async def durdur(self):
        LOGGER(__name__).info(f"Yardımcılar durduruluyor...")
        try:
            if config.STRING1:
                await self.bir.stop()
            if config.STRING2:
                await self.iki.stop()
            if config.STRING3:
                await self.üç.stop()
            if config.STRING4:
                await self.dört.stop()
            if config.STRING5:
                await self.beş.stop()
        except:
            pass

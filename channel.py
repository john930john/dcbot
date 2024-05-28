from pyrogram import filtreler
from pyrogram.enums import SohbetÜyeleriFiltresi, SohbetÜyeDurumu, SohbetTipi
from pyrogram.types import Mesaj

from AnonXMusic import uygulama
from AnonXMusic.utils.veritabanı import c_modunu_ayarla
from AnonXMusic.utils.decorators.admins import YöneticiGerçek
from yapılandırma import YASAKLI_KULLANICILAR


@uygulama.on_message(filtreler.komut(["kanalçal"]) & filtreler.grup & ~YASAKLI_KULLANICILAR)
@YöneticiGerçek
async def çalma_modu(istemci, mesaj: Mesaj, _):
    if len(mesaj.komut) < 2:
        return await mesaj.reply_text(_["ççal_1"].format(mesaj.chat.title))
    sorgu = mesaj.text.split(None, 2)[1].lower().strip()
    if str(sorgu).lower() == "devre dışı":
        await c_modunu_ayarla(mesaj.chat.id, None)
        return await mesaj.reply_text(_["ççal_7"])
    elif str(sorgu) == "bağlantılı":
        sohbet = await uygulama.get_chat(mesaj.chat.id)
        if sohbet.linkli_sohbet:
            sohbet_id = sohbet.linkli_sohbet.id
            await c_modunu_ayarla(mesaj.chat.id, sohbet_id)
            return await mesaj.reply_text(
                _["ççal_3"].format(sohbet.linkli_sohbet.title, sohbet.linkli_sohbet.id)
            )
        else:
            return await mesaj.reply_text(_["ççal_2"])
    else:
        try:
            sohbet = await uygulama.get_chat(sorgu)
        except:
            return await mesaj.reply_text(_["ççal_4"])
        if sohbet.tip != SohbetTipi.KANAL:
            return await mesaj.reply_text(_["ççal_5"])
        try:
            async for kullanıcı in uygulama.get_chat_members(
                sohbet.id, filtre=SohbetÜyeleriFiltresi.YÖNETİCİLER
            ):
                if kullanıcı.durum == SohbetÜyeDurumu.SAHİP:
                    kullanıcı_adı = kullanıcı.kullanıcı.adı
                    kullanıcı_id = kullanıcı.kullanıcı.id
        except:
            return await mesaj.reply_text(_["ççal_4"])
        if kullanıcı_id != mesaj.from_user.id:
            return await mesaj.reply_text(_["ççal_6"].format(sohbet.title, kullanıcı_adı))
        await c_modunu_ayarla(mesaj.chat.id, sohbet.id)
        return await mesaj.reply_text(_["ççal_3"].format(sohbet.title, sohbet.id))
        

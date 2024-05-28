# Telif Hakkı (C) 2024 Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# YT'de Abone Olun < Jankari Ki Dünya >. Tüm hakları saklıdır. © Alexa © Yukki.

""""
TheTeamAlexa, çeşitli amaçlar için Telegram botlarının bir projesidir.
Telif Hakkı (c) 2024 -günümüz Team=Alexa <https://github.com/TheTeamAlexa>

Bu program özgür yazılımdır: yeniden dağıtabilir ve istediğiniz gibi değiştirebilirsiniz veya yeni fikirlere katkıda bulunabilirsiniz.
"""


import config
from config import PRIVATE_BOT_MODE
from AnonXmusic.core.mongo import mongodb

channeldb = mongodb.cplaymode
commanddb = mongodb.komutlar
cleandb = mongodb.temizmod
playmodedb = mongodb.çalma_modu
playtypedb = mongodb.çalma_tipi_db
langdb = mongodb.dil
authdb = mongodb.yöneticiauth
videodb = mongodb.yukkivideogörüşmeleri
onoffdb = mongodb.açıkkapalıper
suggdb = mongodb.öneri
autoenddb = mongodb.otomatikson


# Bellek'e geçiş [mongo sık sık sıkıntı çıkarır]
döngü = {}
çalma_tipi = {}
çalma_modu = {}
kanalbağlantısı = {}
dilmodu = {}
duraklat = {}
sessiz = {}
ses = {}
video = {}
aktif = []
aktifvideo = []
komut = []
temizmod = []
yöneticidışı = {}
vlimit = []
bakım = []
öneri = {}
otomatikson = {}


# Otomatik Bitiş Akışı


async def otomatikson() -> bool:
    sohbet_id = 123
    mod = otomatikson.get(sohbet_id)
    if not mod:
        kullanıcı = await autoenddb.find_one({"sohbet_id": sohbet_id})
        if not kullanıcı:
            otomatikson[sohbet_id] = False
            return False
        otomatikson[sohbet_id] = True
        return True
    return mod


async def otomatikson_aç():
    sohbet_id = 123
    otomatikson[sohbet_id] = True
    kullanıcı = await autoenddb.find_one({"sohbet_id": sohbet_id})
    if not kullanıcı:
        return await autoenddb.insert_one({"sohbet_id": sohbet_id})


async def otomatikson_kapat():
    sohbet_id = 123
    otomatikson[sohbet_id] = False
    kullanıcı = await autoenddb.find_one({"sohbet_id": sohbet_id})
    if kullanıcı:
        return await autoenddb.delete_one({"sohbet_id": sohbet_id})


# ÖNERİ


async def öneri_mi(sohbet_id: int) -> bool:
    mod = öneri.get(sohbet_id)
    if not mod:
        kullanıcı = await suggdb.find_one({"sohbet_id": sohbet_id})
        if not kullanıcı:
            öneri[sohbet_id] = True
            return True
        öneri[sohbet_id] = False
        return False
    return mod


async def öneri_aç(sohbet_id: int):
    öneri[sohbet_id] = True
    kullanıcı = await suggdb.find_one({"sohbet_id": sohbet_id})
    if kullanıcı:
        return await suggdb.delete_one({"sohbet_id": sohbet_id})


async def öneri_kapat(sohbet_id: int):
    öneri[sohbet_id] = False
    kullanıcı = await suggdb.find_one({"sohbet_id": sohbet_id})
    if not kullanıcı:
        return await suggdb.insert_one({"sohbet_id": sohbet_id})


# DÖNGÜ OYNA
async def döngü_ayarla(sohbet_id: int, mod: int):
    döngü[sohbet_id] = mod


# Kanal Oynatma Kimliği
async def kanal_modu_al(sohbet_id: int) -> int:
    mod = kanalbağlantısı.get(sohbet_id)
    if not mod:
        mod = await channeldb.find_one({"sohbet_id": sohbet_id})
        if not mod:
            return None
        kanalbağlantısı[sohbet_id] = mod["mod"]
        return mod["mod"]
    return mod


async def kanal_modu_ayarla(sohbet_id: int, mod: int):
    kanalbağlantısı[sohbet_id] = mod
    await channeldb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"mod": mod}}, upsert=True
    )


# ÇALMA TİPİ YÖNETİMİ SADECE YÖNETİCİLER veya HERKES İÇİN
async def çalma_tipi_al(sohbet_id: int) -> str:
    mod = çalma_tipi.get(sohbet_id)
    if not mod:
        mod = await playtypedb.find_one({"sohbet_id": sohbet_id})
        if not mod:
            çalma_tipi[sohbet_id] = "Herkese"
            return "Herkese"
        çalma_tipi[sohbet_id] = mod["mod"]
        return mod["mod"]
    return mod


async def çalma_tipi_ayarla(sohbet_id: int, mod: str):
    çalma_tipi[sohbet_id] = mod
    await playtypedb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"mod": mod}}, upsert=True
    )


# çalma modu: doğrudan veya çevrimiçi sorgu
async def çalma_modu_al(sohbet_id: int) -> str:
    mod = çalma_modu.get(sohbet_id)
    if not mod:
        mod = await playmodedb.find_one({"sohbet_id": sohbet_id})
        if not mod:
            çalma_modu[sohbet_id] = "Doğrudan"
            return "Doğrudan"
        çalma_modu[sohbet_id] = mod["mod"]
        return mod["mod"]
    return mod


async def çalma_modu_ayarla(sohbet_id: int, mod: str):
    çalma_modu[sohbet_id] = mod
    await playmodedb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"mod": mod}}, upsert=True
    )


# dil
async def dil_al(sohbet_id: int) -> str:
    mod = dilmodu.get(sohbet_id)
    if not mod:
        dil = await langdb.find_one({"sohbet_id": sohbet_id})
        if not dil:
            dilmodu[sohbet_id] = "tr"
            return "tr"
        dilmodu[sohbet_id] = dil["lang"]
        return dil["lang"]
    return mod


async def dil_ayarla(sohbet_id: int, dil: str):
    dilmodu[sohbet_id] = dil
    await langdb.update_one({"sohbet_id": sohbet_id}, {"$set": {"lang": dil}}, upsert=True)


# Sessiz
async def sessiz_mi(sohbet_id: int) -> bool:
    mod = sessiz.get(sohbet_id)
    if not mod:
        return False
    return mod


async def sessiz_aç(sohbet_id: int):
    sessiz[sohbet_id] = True


async def sessiz_kapat(sohbet_id: int):
    sessiz[sohbet_id] = False


# Duraklat-Geç
async def müzik_duraklat(sohbet_id: int) -> bool:
    mod = duraklat.get(sohbet_id)
    if not mod:
        return False
    return mod


async def müzik_duraklat_aç(sohbet_id: int):
    duraklat[sohbet_id] = True


async def müzik_duraklat_kapat(sohbet_id: int):
    duraklat[sohbet_id] = False


# Aktif Sesli Sohbetler
async def aktif_sesli_sohbetler() -> list:
    return aktif


async def aktif_sesli_sohbet_mi(sohbet_id: int) -> bool:
    if sohbet_id not in aktif:
        return False
    else:
        return True


async def aktif_sesli_sohbet_ekle(sohbet_id: int):
    if sohbet_id not in aktif:
        aktif.append(sohbet_id)


async def aktif_sesli_sohbet_kaldır(sohbet_id: int):
    if sohbet_id in aktif:
        aktif.remove(sohbet_id)


# Aktif Video Sohbetler
async def aktif_video_sohbetler() -> list:
    return aktifvideo


async def aktif_video_sohbet_mi(sohbet_id: int) -> bool:
    if sohbet_id not in aktifvideo:
        return False
    else:
        return True


async def aktif_video_sohbet_ekle(sohbet_id: int):
    if sohbet_id not in aktifvideo:
        aktifvideo.append(sohbet_id)


async def aktif_video_sohbet_kaldır(sohbet_id: int):
    if sohbet_id in aktifvideo:
        aktifvideo.remove(sohbet_id)


# Komut Silme Modu
async def komut_silme_modu_aktif_mi(sohbet_id: int) -> bool:
    if sohbet_id not in komut:
        return True
    else:
        return False


async def komut_silme_modu_kapat(sohbet_id: int):
    if sohbet_id not in komut:
        komut.append(sohbet_id)


async def komut_silme_modu_aktif_et(sohbet_id: int):
    try:
        komut.remove(sohbet_id)
    except:
        pass


# Temizleme Modu
async def temizleme_modu_aktif_mi(sohbet_id: int) -> bool:
    if sohbet_id not in temizmod:
        return True
    else:
        return False


async def temizleme_modu_kapat(sohbet_id: int):
    if sohbet_id not in temizmod:
        temizmod.append(sohbet_id)


async def temizleme_modu_aktif_et(sohbet_id: int):
    try:
        temizmod.remove(sohbet_id)
    except:
        pass


# Yönetici Olmayan Sohbet
async def yönetici_olmayan_sohbet_kontrol(sohbet_id: int) -> bool:
    kullanıcı = await authdb.find_one({"sohbet_id": sohbet_id})
    if not kullanıcı:
        return False
    return True


async def yönetici_olmayan_sohbet_mi(sohbet_id: int) -> bool:
    mod = yöneticidışı.get(sohbet_id)
    if not mod:
        kullanıcı = await authdb.find_one({"sohbet_id": sohbet_id})
        if not kullanıcı:
            yöneticidışı[sohbet_id] = False
            return False
        yöneticidışı[sohbet_id] = True
        return True
    return mod


async def yönetici_olmayan_sohbet_ekle(sohbet_id: int):
    yöneticidışı[sohbet_id] = True
    yönetici_mi = await yönetici_olmayan_sohbet_kontrol(sohbet_id)
    if yönetici_mi:
        return
    return await authdb.insert_one({"sohbet_id": sohbet_id})


async def yönetici_olmayan_sohbet_kaldır(sohbet_id: int):
    yöneticidışı[sohbet_id] = False
    yönetici_mi = await yönetici_olmayan_sohbet_kontrol(sohbet_id)
    if not yönetici_mi:
        return
    return await authdb.delete_one({"sohbet_id": sohbet_id})


# Video Limiti
async def video_izinli_mi(sohbet_idd) -> str:
    sohbet_id = 123456
    if not vlimit:
        dblimit = await videodb.find_one({"sohbet_id": sohbet_id})
        if not dblimit:
            vlimit.clear()
            vlimit.append(config.VIDEO_STREAM_LIMIT)
            limit = config.VIDEO_STREAM_LIMIT
        else:
            limit = dblimit["limit"]
            vlimit.clear()
            vlimit.append(limit)
    else:
        limit = vlimit[0]
    if limit == 0:
        return False
    sayı = len(await aktif_video_sohbetler())
    if int(sayı) == int(limit):
        if not await aktif_video_sohbet_mi(sohbet_idd):
            return False
    return True


async def video_limiti_al() -> str:
    sohbet_id = 123456
    if not vlimit:
        dblimit = await videodb.find_one({"sohbet_id": sohbet_id})
        if not dblimit:
            limit = config.VIDEO_STREAM_LIMIT
        else:
            limit = dblimit["limit"]
    else:
        limit = vlimit[0]
    return limit


async def video_limiti_ayarla(limt: int):
    sohbet_id = 123456
    vlimit.clear()
    vlimit.append(limt)
    return await videodb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"limit": limt}}, upsert=True
    )


# Açık Kapalı
async def açıkkapalı(on_off: int) -> bool:
    açık_kapalı = await onoffdb.find_one({"aç_kapa": on_off})
    if not açık_kapalı:
        return False
    return True


async def aç_ekle(aç_kapa: int):
    açık_mı = await açıkkapalı(aç_kapa)
    if açık_mı:
        return
    return await onoffdb.insert_one({"aç_kapa": aç_kapa})


async def kapat(aç_kapa: int):
    kapalı_mı = await açıkkapalı(aç_kapa)
    if not kapalı_mı:
        return
    return await onoffdb.delete_one({"aç_kapa": aç_kapa})


# Bakım


async def bakım_mı():
    if not bakım:
        get = await onoffdb.find_one({"aç_kapa": 1})
        if not get:
            bakım.clear()
            bakım.append(2)
            return True
        else:
            bakım.clear()
            bakım.append(1)
            return False
    else:
        if 1 in bakım:
            return False
        else:
            return True


async def bakım_kapat():
    bakım.clear()
    bakım.append(2)
    kapalı_mı = await açıkkapalı(1)
    if not kapalı_mı:
        return
    return await onoffdb.delete_one({"aç_kapa": 1})


async def bakım_aç():
    bakım.clear()
    bakım.append(1)
    açık_mı = await açıkkapalı(1)
    if açık_mı:
        return
    return await onoffdb.insert_one({"aç_kapa": 1})


# Sesli Video Limiti

from pytgcalls.types import SesParametreleri, SesKalitesi, VideoParametreleri, VideoKalitesi


async def ses_bit_dosyası_kaydet(sohbet_id: int, bit_oranı: str):
    ses[sohbet_id] = bit_oranı


async def video_bit_dosyası_kaydet(sohbet_id: int, bit_oranı: str):
    video[sohbet_id] = bit_oranı


async def ses_bit_ismi_al(sohbet_id: int) -> str:
    mod = ses.get(sohbet_id)
    return "YÜKSEK" if not mod else mod


async def video_bit_ismi_al(sohbet_id: int) -> str:
    mod = video.get(sohbet_id)
    return "FHD_1080p" if not mod else mod


async def ses_bit_oranı_al(sohbet_id: int) -> str:
    mod = ses.get(sohbet_id)
    if not mod:
        return SesParametreleri.kaliteden(SesKalitesi.STÜDYO)
    if str(mod) == "STÜDYO":
        return SesParametreleri.kaliteden(SesKalitesi.STÜDYO)
    elif str(mod) == "YÜKSEK":
        return SesParametreleri.kaliteden(SesKalitesi.YÜKSEK)
    elif str(mod) == "ORTA":
        return SesParametreleri.kaliteden(SesKalitesi.ORTA)
    elif str(mod) == "DÜŞÜK":
        return SesParametreleri.kaliteden(SesKalitesi.DÜŞÜK)


async def video_bit_oranı_al(sohbet_id: int) -> str:
    mod = video.get(sohbet_id)
    if not mod:
        if PRIVATE_BOT_MODE == str(True):
            return VideoParametreleri.kaliteden(VideoKalitesi.FHD_1080p)
        else:
            return VideoParametreleri.kaliteden(VideoKalitesi.HD_720p)
    if str(mod) == "QHD_2K":
        return VideoParametreleri.kaliteden(VideoKalitesi.QHD_2K)
    elif str(mod) == "FHD_1080p":
        return VideoParametreleri.kaliteden(VideoKalitesi.FHD_1080p)
    elif str(mod) == "HD_720p":
        return VideoParametreleri.kaliteden(VideoKalitesi.HD_720p)
    elif str(mod) == "SD_480p":
        return VideoParametreleri.kaliteden(VideoKalitesi.SD_480p)
    elif str(mod) == "SD_360p":
        return VideoParametreleri.kaliteden(VideoKalitesi.SD_360p)
    

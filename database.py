import random
from typing import Dict, List, Union

from AnonXMusic import userbot
from AnonXMusic.core.mongo import mongodb

authdb = mongodb.adminauth
authuserdb = mongodb.authuser
autoenddb = mongodb.autoend
assdb = mongodb.assistants
blacklist_chatdb = mongodb.blacklistChat
blockeddb = mongodb.blockedusers
chatsdb = mongodb.chats
channeldb = mongodb.cplaymode
countdb = mongodb.upcount
cleandb = mongodb.cleanmode
gbansdb = mongodb.gban
langdb = mongodb.language
onoffdb = mongodb.onoffper
playmodedb = mongodb.playmode
playtypedb = mongodb.playtypedb
skipdb = mongodb.skipmode
sudoersdb = mongodb.sudoers
usersdb = mongodb.tgusersdb
queriesdb = mongodb.queries
chattopdb = mongodb.chatstats
privatedb = mongodb.privatechats
playlistdb = mongodb.playlist

# Bellek kullanımı için geçiş [Mongo sık sık sıkıntı çıkarır]
active = []
activevideo = []
assistantdict = {}
autoend = {}
count = {}
channelconnect = {}
langm = {}
loop = {}
maintenance = []
nonadmin = {}
pause = {}
playmode = {}
playtype = {}
skipmode = {}


async def asistan_numarasını_al(chat_id: int) -> str:
    asistan = assistantdict.get(chat_id)
    return asistan


async def istemciyi_al(asistan: int):
    if int(asistan) == 1:
        return userbot.one
    elif int(asistan) == 2:
        return userbot.two
    elif int(asistan) == 3:
        return userbot.three
    elif int(asistan) == 4:
        return userbot.four
    elif int(asistan) == 5:
        return userbot.five


async def yeni_asistan_ayarla(sohbet_id, numara):
    numara = int(numara)
    await assdb.update_one(
        {"sohbet_id": sohbet_id},
        {"$set": {"asistan": numara}},
        upsert=True,
    )


async def asistan_ayarla(sohbet_id):
    userbot_listesi = await istemciyi_al(random.randint(1, 5))
    ran_asistan = random.choice(userbot_listesi)
    assistantdict[sohbet_id] = ran_asistan
    await assdb.update_one(
        {"sohbet_id": sohbet_id},
        {"$set": {"asistan": ran_asistan}},
        upsert=True,
    )
    return ran_asistan


async def asistan_al(sohbet_id: int) -> str:
    asistan = assistantdict.get(sohbet_id)
    if not asistan:
        db_asistan = await assdb.find_one({"sohbet_id": sohbet_id})
        if not db_asistan:
            userbot = await asistan_ayarla(sohbet_id)
            return userbot
        else:
            alınan_asistan = db_asistan["asistan"]
            if alınan_asistan in userbot_listesi:
                assistantdict[sohbet_id] = alınan_asistan
                userbot = await istemciyi_al(alınan_asistan)
                return userbot
            else:
                userbot = await asistan_ayarla(sohbet_id)
                return userbot
    else:
        if asistan in userbot_listesi:
            userbot = await istemciyi_al(asistan)
            return userbot
        else:
            userbot = await asistan_ayarla(sohbet_id)
            return userbot


async def çağrılar_asistan(sohbet_id):
    userbot_listesi = await istemciyi_al(random.randint(1, 5))
    ran_asistan = random.choice(userbot_listesi)
    assistantdict[sohbet_id] = ran_asistan
    await assdb.update_one(
        {"sohbet_id": sohbet_id},
        {"$set": {"asistan": ran_asistan}},
        upsert=True,
    )
    return ran_asistan


async def grup_asistanı(self, sohbet_id: int) -> int:
    asistan = assistantdict.get(sohbet_id)
    if not asistan:
        db_asistan = await assdb.find_one({"sohbet_id": sohbet_id})
        if not db_asistan:
            asis = await çağrılar_asistan(sohbet_id)
        else:
            asis = db_asistan["asistan"]
            if asis in userbot_listesi:
                assistantdict[sohbet_id] = asis
                asis = asis
            else:
                asis = await çağrılar_asistan(sohbet_id)
    else:
        if asistan in userbot_listesi:
            asis = asistan
        else:
            asis = await çağrılar_asistan(sohbet_id)
    if int(asis) == 1:
        return self.one
    elif int(asis) == 2:
        return self.two
    elif int(asis) == 3:
        return self.three
    elif int(asis) == 4:
        return self.four
    elif int(asis) == 5:
        return self.five


async def atla_modu_aktif_mi(sohbet_id: int) -> bool:
    mod = skipmode.get(sohbet_id)
    if not mod:
        kullanıcı = await skipdb.find_one({"sohbet_id": sohbet_id})
        if not kullanıcı:
            skipmode[sohbet_id] = True
            return True
        skipmode[sohbet_id] = False
        return False
    return mod


async def atla_modunu_aktif_et(sohbet_id: int):
    skipmode[sohbet_id] = True
    kullanıcı = await skipdb.find_one({"sohbet_id": sohbet_id})
    if kullanıcı:
        return await skipdb.delete_one({"sohbet_id": sohbet_id})


async def atla_modunu_kapat(sohbet_id: int):
    skipmode[sohbet_id] = False
    kullanıcı = await skipdb.find_one({"sohbet_id": sohbet_id})
    if not kullanıcı:
        return await skipdb.insert_one({"sohbet_id": sohbet_id})


async def oy_sayısını_al(sohbet_id: int) -> int:
    mod = count.get(sohbet_id)
    if not mod:
        mod = await countdb.find_one({"sohbet_id": sohbet_id})
        if not mod:
            return 5
        count[sohbet_id] = mod["mod"]
        return mod["mod"]
    return mod


async def oyları_ayarla(sohbet_id: int, mod: int):
    count[sohbet_id] = mod
    await countdb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"mod": mod}}, upsert=True
    )


async def otomatik_sonlandırma_aktif_mi() -> bool:
    sohbet_id = 1234
    kullanıcı = await autoenddb.find_one({"sohbet_id": sohbet_id})
    if not kullanıcı:
        return False
    return True


async def otomatik_sonlandırma_aktif_et():
    sohbet_id = 1234
    await autoenddb.insert_one({"sohbet_id": sohbet_id})


async def otomatik_sonlandırma_kapat():
    sohbet_id = 1234
    await autoenddb.delete_one({"sohbet_id": sohbet_id})


async def döngüyü_al(sohbet_id: int) -> int:
    döngü = loop.get(sohbet_id)
    if not döngü:
        return 0
    return döngü


async def döngüyü_ayarla(sohbet_id: int, mod: int):
    loop[sohbet_id] = mod


async def bağlantı_modunu_al(sohbet_id: int) -> int:
    mod = channelconnect.get(sohbet_id)
    if not mod:
        mod = await channeldb.find_one({"sohbet_id": sohbet_id})
        if not mod:
            return None
        channelconnect[sohbet_id] = mod["mod"]
        return mod["mod"]
    return mod


async def bağlantı_modunu_ayarla(sohbet_id: int, mod: int):
    channelconnect[sohbet_id] = mod
    await channeldb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"mod": mod}}, upsert=True
    )


async def çalma_tipini_al(sohbet_id: int) -> str:
    mod = playtype.get(sohbet_id)
    if not mod:
        mod = await playtypedb.find_one({"sohbet_id": sohbet_id})
        if not mod:
            playtype[sohbet_id] = "Herkes"
            return "Herkes"
        playtype[sohbet_id] = mod["mod"]
        return mod["mod"]
    return mod


async def çalma_tipini_ayarla(sohbet_id: int, mod: str):
    playtype[sohbet_id] = mod
    await playtypedb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"mod": mod}}, upsert=True
    )


async def çalma_modunu_al(sohbet_id: int) -> str:
    mod = playmode.get(sohbet_id)
    if not mod:
        mod = await playmodedb.find_one({"sohbet_id": sohbet_id})
        if not mod:
            playmode[sohbet_id] = "Doğrudan"
            return "Doğrudan"
        playmode[sohbet_id] = mod["mod"]
        return mod["mod"]
    return mod


async def çalma_modunu_ayarla(sohbet_id: int, mod: str):
    playmode[sohbet_id] = mod
    await playmodedb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"mod": mod}}, upsert=True
    )


async def sorguları_al() -> int:
    sohbet_id = 98324
    mod = await queriesdb.find_one({"sohbet_id": sohbet_id})
    if not mod:
        return 0
    return mod["mod"]


async def sorguları_ayarla(mod: int):
    sohbet_id = 98324
    queries = await queriesdb.find_one({"sohbet_id": sohbet_id})
    if queries:
        mod = queries["mod"] + mod
    return await queriesdb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"mod": mod}}, upsert=True
    )

async def dil_al(sohbet_id: int) -> str:
    mod = langm.get(sohbet_id)
    if not mod:
        dil = await langdb.find_one({"sohbet_id": sohbet_id})
        if not dil:
            langm[sohbet_id] = "tr"
            return "tr"
        langm[sohbet_id] = dil["mod"]
        return dil["mod"]
    return mod


async def dil_ayarla(sohbet_id: int, dil: str):
    langm[sohbet_id] = dil
    await langdb.update_one(
        {"sohbet_id": sohbet_id}, {"$set": {"mod": dil}}, upsert=True
    )


async def kullanıcı_dilini_al(kullanıcı: Union[int, str]) -> str:
    dil = await langdb.find_one({"sohbet_id": kullanıcı})
    if not dil:
        return "tr"
    return dil["mod"]


async def kullanıcı_dilini_ayarla(kullanıcı: Union[int, str], dil: str):
    await langdb.update_one(
        {"sohbet_id": kullanıcı}, {"$set": {"mod": dil}}, upsert=True
    )


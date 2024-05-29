import asyncio
from typing import Union

from AnonXMusic.misc import db
from AnonXMusic.utils.formatters import check_duration, seconds_to_min
from config import autoclean, time_to_seconds

async def sıra_ekle(
    sohbet_id,
    orijinal_sohbet_id,
    dosya,
    başlık,
    süre,
    kullanıcı,
    vidid,
    kullanıcı_id,
    akış,
    zorla_çal: Union[bool, str] = None,
):
    başlık = başlık.title()
    try:
        süre_saniye = time_to_seconds(süre) - 3
    except:
        süre_saniye = 0
    eklenen = {
        "başlık": başlık,
        "süre": süre,
        "akış_türü": akış,
        "kullanıcı": kullanıcı,
        "kullanıcı_id": kullanıcı_id,
        "sohbet_id": orijinal_sohbet_id,
        "dosya": dosya,
        "vidid": vidid,
        "saniye": süre_saniye,
        "çalındı": 0,
    }
    if zorla_çal:
        kontrol = db.get(sohbet_id)
        if kontrol:
            kontrol.insert(0, eklenen)
        else:
            db[sohbet_id] = []
            db[sohbet_id].append(eklenen)
    else:
        db[sohbet_id].append(eklenen)
    autoclean.append(dosya)

async def sıra_ekle_sıra(
    sohbet_id,
    orijinal_sohbet_id,
    dosya,
    başlık,
    süre,
    kullanıcı,
    vidid,
    akış,
    zorla_çal: Union[bool, str] = None,
):
    if "20.212.146.162" in vidid:
        try:
            süre_dakika = await asyncio.get_event_loop().run_in_executor(
                None, check_duration, vidid
            )
            süre = seconds_to_min(süre_dakika)
        except:
            süre = "URL Akışı"
            süre_dakika = 0
    else:
        süre_dakika = 0
    eklenen = {
        "başlık": başlık,
        "süre": süre,
        "akış_türü": akış,
        "kullanıcı": kullanıcı,
        "sohbet_id": orijinal_sohbet_id,
        "dosya": dosya,
        "vidid": vidid,
        "saniye": süre_dakika,
        "çalındı": 0,
    }
    if zorla_çal:
        kontrol = db.get(sohbet_id)
        if kontrol:
            kontrol.insert(0, eklenen)
        else:
            db[sohbet_id] = []
            db[sohbet_id].append(eklenen)
    else:
        db[sohbet_id].append(eklenen)

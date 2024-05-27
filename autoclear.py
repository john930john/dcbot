import os

from config import otomatik_temizle


async def otomatik_temizle(poplanan):
    try:
        silinecek = poplanan["file"]
        otomatik_temizle.remove(silinecek)
        sayı = otomatik_temizle.count(silinecek)
        if sayı == 0:
            if "vid_" not in silinecek or "canlı_" not in silinecek or "indeks_" not in silinecek:
                try:
                    os.remove(silinecek)
                except:
                    pass
    except:
        pass
        

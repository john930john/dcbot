import os
import re

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch

from AnonXMusic import app
from config import YOUTUBE_IMG_URL


def resimBoyutunuDeğiştir(maksGenişlik, maksYükseklik, resim):
    genişlikOranı = maksGenişlik / resim.size[0]
    yükseklikOranı = maksYükseklik / resim.size[1]
    yeniGenişlik = int(genişlikOranı * resim.size[0])
    yeniYükseklik = int(yükseklikOranı * resim.size[1])
    yeniResim = resim.resize((yeniGenişlik, yeniYükseklik))
    return yeniResim


def temizle(metin):
    liste = metin.split(" ")
    başlık = ""
    for kelime in liste:
        if len(başlık) + len(kelime) < 60:
            başlık += " " + kelime
    return başlık.strip()


async def videoKapakAl(videoID):
    if os.path.isfile(f"cache/{videoID}.png"):
        return f"cache/{videoID}.png"

    url = f"https://www.youtube.com/watch?v={videoID}"
    try:
        sonuçlar = VideosSearch(url, limit=1)
        for sonuç in (await sonuçlar.next())["result"]:
            try:
                başlık = sonuç["title"]
                başlık = re.sub("\W+", " ", başlık)
                başlık = başlık.title()
            except:
                başlık = "Desteklenmeyen Başlık"
            try:
                süre = sonuç["duration"]
            except:
                süre = "Bilinmeyen Dakikalar"
            kapakResmi = sonuç["thumbnails"][0]["url"].split("?")[0]
            try:
                görüntülenme = sonuç["viewCount"]["short"]
            except:
                görüntülenme = "Bilinmeyen Görüntülenme"
            try:
                kanal = sonuç["channel"]["name"]
            except:
                kanal = "Bilinmeyen Kanal"

        async with aiohttp.ClientSession() as oturum:
            async with oturum.get(kapakResmi) as yanıt:
                if yanıt.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoID}.png", mode="wb")
                    await f.write(await yanıt.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoID}.png")
        resim1 = resimBoyutunuDeğiştir(1280, 720, youtube)
        resim2 = resim1.convert("RGBA")
        arkaplan = resim2.filter(filter=ImageFilter.BoxBlur(10))
        parlaklıkGeliştirici = ImageEnhance.Brightness(arkaplan)
        arkaplan = parlaklıkGeliştirici.enhance(0.5)
        çiz = ImageDraw.Draw(arkaplan)
        arial = ImageFont.truetype("AnonXMusic/assets/font2.ttf", 30)
        font = ImageFont.truetype("AnonXMusic/assets/font.ttf", 30)
        çiz.text((1110, 8), unidecode(app.name), fill="white", font=arial)
        çiz.text(
            (55, 560),
            f"{kanal} | {görüntülenme[:23]}",
            (255, 255, 255),
            font=arial,
        )
        çiz.text(
            (57, 600),
            temizle(başlık),
            (255, 255, 255),
            font=font,
        )
        çiz.line(
            [(55, 660), (1220, 660)],
            fill="white",
            width=5,
            joint="curve",
        )
        çiz.ellipse(
            [(918, 648), (942, 672)],
            outline="white",
            fill="white",
            width=15,
        )
        çiz.text(
            (36, 685),
            "00:00",
            (255, 255, 255),
            font=arial,
        )
        çiz.text(
            (1185, 685),
            f"{süre[:23]}",
            (255, 255, 255),
            font=arial,
        )
        try:
            os.remove(f"cache/thumb{videoID}.png")
        except:
            pass
        arkaplan.save(f"cache/{videoID}.png")
        return f"cache/{videoID}.png"
    except Exception as hata:
        print(hata)
        return YOUTUBE_IMG_URL
    

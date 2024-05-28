import os
import re
import subprocess
import sys
import traceback
from inspect import getfullargspec
from io import StringIO
from time import time

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from AnonXMusic import app
from config import OWNER_ID


async def aexec(kod, istemci, mesaj):
    exec(
        "async def __aexec(istemci, mesaj): "
        + "".join(f"\n {a}" for a in kod.split("\n"))
    )
    return await locals()["__aexec"](istemci, mesaj)


async def düzenle_ya_da_yanıtla(msj: Message, **kwargs):
    func = msj.edit_text if msj.from_user.is_self else msj.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})


@app.on_edited_message(
    filters.command("değerlendir")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
@app.on_message(
    filters.command("değerlendir")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def yürütücü(istemci: app, mesaj: Message):
    if len(mesaj.command) < 2:
        return await düzenle_ya_da_yanıtla(mesaj, text="<b>Ne yürütmek istiyorsun?</b>")
    try:
        komut = mesaj.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await mesaj.delete()
    t1 = time()
    eski_stderr = sys.stderr
    eski_stdout = sys.stdout
    yönlendirilmiş_çıktı = sys.stdout = StringIO()
    yönlendirilmiş_hata = sys.stderr = StringIO()
    çıktı, hata, exc = None, None, None
    try:
        await aexec(komut, istemci, mesaj)
    except Exception:
        exc = traceback.format_exc()
    çıktı = yönlendirilmiş_çıktı.getvalue()
    hata = yönlendirilmiş_hata.getvalue()
    sys.stdout = eski_stdout
    sys.stderr = eski_stderr
    değerlendirme = "\n"
    if exc:
        değerlendirme += exc
    elif hata:
        değerlendirme += hata
    elif çıktı:
        değerlendirme += çıktı
    else:
        değerlendirme += "Başarılı"
    son_çıktı = f"<b>⥤ Sonuç :</b>\n<pre language='python'>{değerlendirme}</pre>"
    if len(son_çıktı) > 4096:
        dosya_adı = "çıktı.txt"
        with open(dosya_adı, "w+", encoding="utf8") as out_file:
            out_file.write(str(değerlendirme))
        t2 = time()
        klavye = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⏳",
                        callback_data=f"çalışmasüresi {t2-t1} Saniye",
                    )
                ]
            ]
        )
        await mesaj.reply_document(
            document=dosya_adı,
            caption=f"<b>⥤ Değerlendir :</b>\n<code>{komut[0:980]}</code>\n\n<b>⥤ Sonuç :</b>\nEkli Belge",
            quote=False,
            reply_markup=klavye,
        )
        await mesaj.delete()
        os.remove(dosya_adı)
    else:
        t2 = time()
        klavye = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⏳",
                        callback_data=f"çalışmasüresi {round(t2-t1, 3)} Saniye",
                    ),
                    InlineKeyboardButton(
                        text="🗑",
                        callback_data=f"forceclose abc|{mesaj.from_user.id}",
                    ),
                ]
            ]
        )
        await düzenle_ya_da_yanıtla(mesaj, text=son_çıktı, reply_markup=klavye)


@app.on_callback_query(filters.regex(r"çalışmasüresi"))
async def çalışmasüresi_fonk_cq(_, cq):
    çalışmasüresi = cq.data.split(None, 1)[1]
    await cq.answer(çalışmasüresi, show_alert=True)


@app.on_callback_query(filters.regex("forceclose"))
async def forceclose_command(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    sorgu, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "» Sınırlarında kalmak daha iyi olurdu.",
                show_alert=True
            )
        except:
            return
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        return


@app.on_edited_message(
    filters.command("sh")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
@app.on_message(
    filters.command("sh")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def shellrunner(_, mesaj: Message):
    if len(mesaj.command) < 2:
        return await düzenle_ya_da_yanıtla(
            mesaj, text="<b>Örnek :</b>\n/sh git pull"
        )
    metin = mesaj.text.split(None, 1)[1]
    if "\n" in metin:
        kod = metin.split("\n")
        çıktı = ""
        for x in kod:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
            try:
                process = subprocess.Popen(
                    shell,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            except Exception as err:
                await düzenle_ya_da_yanıtla(
                    mesaj, text=f"<b>HATA :</b>\n<pre>{err}</pre>"
                )
            çıktı += f"<b>{kod}</b>\n"
            çıktı += process.stdout.read()[:-1].decode("utf-8")
            çıktı += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", metin)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except Exception as err:
            print(err)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            hatalar = traceback.format_exception(
                etype=exc_type,
                value=exc_obj,
                tb=exc_tb,
            )
            return await düzenle_ya_da_yanıtla(
                mesaj, text=f"<b>HATA :</b>\n<pre>{''.join(hatalar)}</pre>"
            )
        çıktı = process.stdout.read()[:-1].decode("utf-8")
    if str(çıktı) == "\n":
        çıktı = None
    if çıktı:
        if len(çıktı) > 4096:
            with open("çıktı.txt", "w+") as dosya:
                dosya.write(çıktı)
            await app.send_document(
                mesaj.chat.id,
                "çıktı.txt",
                reply_to_message_id=mesaj.id,
                caption="<code>Çıktı</code>",
            )
            return os.remove("çıktı.txt")
        await düzenle_ya_da_yanıtla(mesaj, text=f"<b>ÇIKTI :</b>\n<pre>{çıktı}</pre>")
    else:
        await düzenle_ya_da_yanıtla(mesaj, text="<b>ÇIKTI :</b>\n<code>Yok</code>")
    await mesaj.stop_propagation()
        

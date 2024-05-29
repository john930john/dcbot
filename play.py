import math

from pyrogram.types import InlineKeyboardButton

from AnonXMusic.utils.formatters import time_to_seconds


def takip_düzeni(_, videoid, kullanıcı_id, kanal, fplay):
    düğmeler = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{kullanıcı_id}|a|{kanal}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{kullanıcı_id}|v|{kanal}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{kullanıcı_id}",
            )
        ],
    ]
    return düğmeler


def akış_düzeni_zamanlayıcı(_, sohbet_id, oynatılan, dur):
    oynatılan_saniye = time_to_seconds(oynatılan)
    süre_saniye = time_to_seconds(dur)
    yüzde = (oynatılan_saniye / süre_saniye) * 100
    yuvarlanmış_yüzde = math.floor(yüzde)
    if 0 < yuvarlanmış_yüzde <= 10:
        çubuk = "◉—————————"
    elif 10 < yuvarlanmış_yüzde < 20:
        çubuk = "—◉————————"
    elif 20 <= yuvarlanmış_yüzde < 30:
        çubuk = "——◉———————"
    elif 30 <= yuvarlanmış_yüzde < 40:
        çubuk = "———◉——————"
    elif 40 <= yuvarlanmış_yüzde < 50:
        çubuk = "————◉—————"
    elif 50 <= yuvarlanmış_yüzde < 60:
        çubuk = "—————◉————"
    elif 60 <= yuvarlanmış_yüzde < 70:
        çubuk = "——————◉———"
    elif 70 <= yuvarlanmış_yüzde < 80:
        çubuk = "———————◉——"
    elif 80 <= yuvarlanmış_yüzde < 95:
        çubuk = "————————◉—"
    else:
        çubuk = "—————————◉"
    düğmeler = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{sohbet_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{sohbet_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{sohbet_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{sohbet_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{sohbet_id}"),
        ],
        [
            InlineKeyboardButton(
                text=f"{oynatılan} {çubuk} {dur}",
                callback_data="GetTimer",
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return düğmeler


def akış_düzeni(_, sohbet_id):
    düğmeler = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{sohbet_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{sohbet_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{sohbet_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{sohbet_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{sohbet_id}"),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return düğmeler


def çalma_listesi_düzeni(_, videoid, kullanıcı_id, ptype, kanal, fplay):
    düğmeler = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonyPlaylists {videoid}|{kullanıcı_id}|{ptype}|a|{kanal}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonyPlaylists {videoid}|{kullanıcı_id}|{ptype}|v|{kanal}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{kullanıcı_id}",
            ),
        ],
    ]
    return düğmeler


def canlı_akış_düzeni(_, videoid, kullanıcı_id, mod, kanal, fplay):
    düğmeler = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{kullanıcı_id}|{mod}|{kanal}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{kullanıcı_id}",
            ),
        ],
    ]
    return düğmeler


def kaydırıcı_düzeni(_, videoid, kullanıcı_id, sorgu, sorgu_tipi, kanal, fplay):
    sorgu = f"{sorgu[:20]}"
    düğmeler = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{kullanıcı_id}|a|{kanal}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{kullanıcı_id}|v|{kanal}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{sorgu_tipi}|{sorgu}|{kullanıcı_id}|{kanal}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {sorgu}|{kullanıcı_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{sorgu_tipi}|{sorgu}|{kullanıcı_id}|{kanal}|{fplay}",
            ),
        ],
    ]
    return düğmeler
                      

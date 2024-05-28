from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ayarlar import DESTEK_SOHBETI


def bot_çalma_listesi_düğmeleri(dil):
    düğmeler = [
        [
            InlineKeyboardButton(text=dil["S_B_9"], url=DESTEK_SOHBETI),
            InlineKeyboardButton(text=dil["KAPATMA_DÜĞMESİ"], callback_data="kapat"),
        ],
    ]
    return düğmeler


def kapat_düğmeleri(dil):
    düğmeler = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=dil["KAPATMA_DÜĞMESİ"],
                    callback_data="kapat",
                ),
            ]
        ]
    )
    return düğmeler


def destek_düğmeleri(dil):
    düğmeler = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=dil["S_B_9"],
                    url=DESTEK_SOHBETI,
                ),
            ]
        ]
    )
    return düğmeler
    

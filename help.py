from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonXMusic import app


def yardım_paneli(_, BAŞLANGIÇ: Union[bool, int] = None):
    ilk = [InlineKeyboardButton(text=_["KAPAT_BUTTON"], callback_data=f"kapat")]
    ikinci = [
        InlineKeyboardButton(
            text=_["GERİ_BUTTON"],
            callback_data=f"ayarlar_geri_yardımcı",
        ),
    ]
    işaret = ikinci if BAŞLANGIÇ else ilk
    düzen = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["Y_B_1"],
                    callback_data="yardım_callback yb1",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_2"],
                    callback_data="yardım_callback yb2",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_3"],
                    callback_data="yardım_callback yb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["Y_B_4"],
                    callback_data="yardım_callback yb4",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_5"],
                    callback_data="yardım_callback yb5",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_6"],
                    callback_data="yardım_callback yb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["Y_B_7"],
                    callback_data="yardım_callback yb7",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_8"],
                    callback_data="yardım_callback yb8",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_9"],
                    callback_data="yardım_callback yb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["Y_B_10"],
                    callback_data="yardım_callback yb10",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_11"],
                    callback_data="yardım_callback yb11",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_12"],
                    callback_data="yardım_callback yb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["Y_B_13"],
                    callback_data="yardım_callback yb13",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_14"],
                    callback_data="yardım_callback yb14",
                ),
                InlineKeyboardButton(
                    text=_["Y_B_15"],
                    callback_data="yardım_callback yb15",
                ),
            ],
            işaret,
        ]
    )
    return düzen


def yardım_geri_düzen(_):
    düzen = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["GERİ_BUTTON"],
                    callback_data=f"ayarlar_geri_yardımcı",
                ),
            ]
        ]
    )
    return düzen


def özel_yardım_paneli(_):
    düğmeler = [
        [
            InlineKeyboardButton(
                text=_["Ö_B_4"],
                url=f"https://t.me/{app.username}?start=yardım",
            ),
        ],
    ]
    return düğmeler
    

from typing import Union

from pyrogram.types import InlineKeyboardButton


def ayar_markup(dil):
    buttons = [
        [
            InlineKeyboardButton(text=dil["ST_B_1"], callback_data="AU"),
            InlineKeyboardButton(text=dil["ST_B_3"], callback_data="LG"),
        ],
        [
            InlineKeyboardButton(text=dil["ST_B_2"], callback_data="PM"),
        ],
        [
            InlineKeyboardButton(text=dil["ST_B_4"], callback_data="VM"),
        ],
        [
            InlineKeyboardButton(text=dil["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def oy_modu_ayarları(dil, şuanki, mod: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="Oy Modu ➜", callback_data="VOTEANSWER"),
            InlineKeyboardButton(
                text=dil["ST_B_5"] if mod == True else dil["ST_B_6"],
                callback_data="VOMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text="-2", callback_data="FERRARIUDTI M"),
            InlineKeyboardButton(
                text=f"şuanki : {şuanki}",
                callback_data="ANSWERVOMODE",
            ),
            InlineKeyboardButton(text="+2", callback_data="FERRARIUDTI A"),
        ],
        [
            InlineKeyboardButton(
                text=dil["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text=dil["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def yetkililer_ayarları(dil, durum: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text=dil["ST_B_7"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=dil["ST_B_8"] if durum == True else dil["ST_B_9"],
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(text=dil["ST_B_1"], callback_data="AUTHLIST"),
        ],
        [
            InlineKeyboardButton(
                text=dil["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text=dil["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def çalma_modu_ayarları(
    dil,
    Direkt: Union[bool, str] = None,
    Grup: Union[bool, str] = None,
    Oynatma_tipi: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(text=dil["ST_B_10"], callback_data="SEARCHANSWER"),
            InlineKeyboardButton(
                text=dil["ST_B_11"] if Direkt == True else dil["ST_B_12"],
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=dil["ST_B_13"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=dil["ST_B_8"] if Grup == True else dil["ST_B_9"],
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=dil["ST_B_14"], callback_data="PLAYTYPEANSWER"),
            InlineKeyboardButton(
                text=dil["ST_B_8"] if Oynatma_tipi == True else dil["ST_B_9"],
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=dil["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text=dil["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
    

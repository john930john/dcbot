from pyrogram.types import InlineKeyboardButton
import config

def şarkı_seçimi(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"şarkı_yardımcısı ses|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"şarkı_yardımcısı video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥀 Destek 🥀", url=f"{config.DESTEK_SOHBETİ}",
            ),
            InlineKeyboardButton(
                text=_["KAPAT"], callback_data="kapat"
            ),
        ],
    ]
    return buttons
    

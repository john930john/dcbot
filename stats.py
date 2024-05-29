from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def istatistik_düğmeleri(_, durum):
    sudo_yok = [
        InlineKeyboardButton(
            text=_["SA_B_1"],
            callback_data="TopOverall",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_2"],
            callback_data="bot_stats_sudo",
        ),
        InlineKeyboardButton(
            text=_["SA_B_3"],
            callback_data="TopOverall",
        ),
    ]
    düzenle = sudo if durum else sudo_yok
    düğmeler = InlineKeyboardMarkup(
        [
            düzenle,
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return düğmeler


def geri_istatistik_düğmeleri(_):
    düğmeler = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="stats_back",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return düğmeler
    

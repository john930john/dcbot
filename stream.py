import os
from random import randint
from typing import Union

from pyrogram.types import InlineKeyboardMarkup

import config
from AnonXMusic import Carbon, YouTube, app
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import db
from AnonXMusic.utils.database import add_active_video_chat, is_active_chat
from AnonXMusic.utils.exceptions import AssistantErr
from AnonXMusic.utils.inline import aq_markup, close_markup, stream_markup
from AnonXMusic.utils.pastebin import AnonyBin
from AnonXMusic.utils.stream.queue import put_queue, put_queue_index
from AnonXMusic.utils.thumbnails import get_thumb


async def akış(
    _,
    mystic,
    user_id,
    result,
    chat_id,
    user_name,
    original_chat_id,
    video: Union[bool, str] = None,
    akış_türü: Union[bool, str] = None,
    spotify: Union[bool, str] = None,
    zorla_çal: Union[bool, str] = None,
):
    if not result:
        return
    if zorla_çal:
        await Anony.force_stop_stream(chat_id)
    if akış_türü == "çalma listesi":
        msg = f"{_['play_19']}\n\n"
        count = 0
        for search in result:
            if int(count) == config.PLAYLIST_FETCH_LIMIT:
                continue
            try:
                (
                    başlık,
                    süre_dakika,
                    süre_saniye,
                    kapak,
                    vidid,
                ) = await YouTube.details(search, False if spotify else True)
            except:
                continue
            if str(süre_dakika) == "None":
                continue
            if süre_saniye > config.DURATION_LIMIT:
                continue
            if await is_active_chat(chat_id):
                await put_queue(
                    chat_id,
                    original_chat_id,
                    f"vid_{vidid}",
                    başlık,
                    süre_dakika,
                    user_name,
                    vidid,
                    user_id,
                    "video" if video else "audio",
                )
                position = len(db.get(chat_id)) - 1
                count += 1
                msg += f"{count}. {başlık[:70]}\n"
                msg += f"{_['play_20']} {position}\n\n"
            else:
                if not zorla_çal:
                    db[chat_id] = []
                durum = True if video else None
                try:
                    dosya_yolu, doğrudan = await YouTube.download(
                        vidid, mystic, video=durum, videoid=True
                    )
                except:
                    raise AssistantErr(_["play_14"])
                await Anony.join_call(
                    chat_id,
                    original_chat_id,
                    dosya_yolu,
                    video=durum,
                    image=kapak,
                )
                await put_queue(
                    chat_id,
                    original_chat_id,
                    dosya_yolu if doğrudan else f"vid_{vidid}",
                    başlık,
                    süre_dakika,
                    user_name,
                    vidid,
                    user_id,
                    "video" if video else "audio",
                    zorla_çal=zorla_çal,
                )
                img = await get_thumb(vidid)
                button = stream_markup(_, chat_id)
                run = await app.send_photo(
                    original_chat_id,
                    photo=img,
                    caption=_["stream_1"].format(
                        f"https://t.me/{app.username}?start=info_{vidid}",
                        başlık[:23],
                        süre_dakika,
                        user_name,
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "stream"
        if count == 0:
            return
        else:
            link = await AnonyBin(msg)
            lines = msg.count("\n")
            if lines >= 17:
                car = os.linesep.join(msg.split(os.linesep)[:17])
            else:
                car = msg
            carbon = await Carbon.generate(car, randint(100, 10000000))
            upl = close_markup(_)
            return await app.send_photo(
                original_chat_id,
                photo=carbon,
                caption=_["play_21"].format(position, link),
                reply_markup=upl,
            )
    elif akış_türü == "youtube":
        link = result["link"]
        vidid = result["vidid"]
        başlık = (result["title"]).title()
        süre_dakika = result["duration_min"]
        kapak = result["thumb"]
        durum = True if video else None
        try:
            dosya_yolu, doğrudan = await YouTube.download(
                vidid, mystic, videoid=True, video=durum
            )
        except:
            raise AssistantErr(_["play_14"])
        if await is_active_chat(chat_id):
            await put_queue(
                chat_id,
                original_chat_id,
                dosya_yolu if doğrudan else f"vid_{vidid}",
                başlık,
                süre_dakika,
                user_name,
                vidid,
                user_id,
                "video" if video else "audio",
            )
            position = len(db.get(chat_id)) - 1
            button = aq_markup(_, chat_id)
            await app.send_message(
                chat_id=original_chat_id,
                text=_["queue_4"].format(position, başlık[:27], süre_dakika, user_name),
                reply_markup=InlineKeyboardMarkup(button),
            )
        else:
            if not zorla_çal:
                db[chat_id] = []
            await Anony.join_call(
                chat_id,
                original_chat_id,
                dosya_yolu,
                video=durum,
                image=kapak,
            )
            await put_queue(
                chat_id,
                original_chat_id,
                dosya_yolu if doğrudan else f"vid_{vidid}",
                başlık,
                süre_dakika,
                user_name,
                vidid,
                user_id,
                "video" if video else "audio",
                zorla_çal=zorla_çal,
            )
            img = await get_thumb(vidid)
            button = stream_markup(_, chat_id)
            run = await app.send_photo(
                original_chat_id,
                photo=img,
                caption=_["stream_1"].format(
                    f"https://t.me/{app.username}?start=info_{vidid}",
                    başlık[:23],
                    süre_dakika,
                    user_name,
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
    elif akış_türü == "soundcloud":
        dosya_yolu =
        

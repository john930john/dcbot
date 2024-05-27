from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.utils import extract_user, int_to_alpha
from AnonXMusic.utils.database import (
    delete_authuser,
    get_authuser,
    get_authuser_names,
    save_authuser,
)
from AnonXMusic.utils.decorators import AdminActual, language
from AnonXMusic.utils.inline import close_markup
from config import BANNED_USERS, adminlist


@app.on_message(filters.command("yetkilendir") & filters.group & ~BANNED_USERS)
@AdminActual
@language
async def yetkilendir(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["genel_1"])
    user = await extract_user(message)
    token = await int_to_alpha(user.id)
    _check = await get_authuser_names(message.chat.id)
    count = len(_check)
    if int(count) == 25:
        return await message.reply_text(_["yetkilendirme_1"])
    if token not in _check:
        assis = {
            "auth_user_id": user.id,
            "auth_name": user.first_name,
            "admin_id": message.from_user.id,
            "admin_name": message.from_user.first_name,
        }
        get = adminlist.get(message.chat.id)
        if get:
            if user.id not in get:
                get.append(user.id)
        await save_authuser(message.chat.id, token, assis)
        return await message.reply_text(_["yetkilendirme_2"].format(user.mention))
    else:
        return await message.reply_text(_["yetkilendirme_3"].format(user.mention))


@app.on_message(filters.command("yetkikaldır") & filters.group & ~BANNED_USERS)
@AdminActual
@language
async def yetkikaldır(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["genel_1"])
    user = await extract_user(message)
    token = await int_to_alpha(user.id)
    deleted = await delete_authuser(message.chat.id, token)
    get = adminlist.get(message.chat.id)
    if get:
        if user.id in get:
            get.remove(user.id)
    if deleted:
        return await message.reply_text(_["yetkikaldırma_1"].format(user.mention))
    else:
        return await message.reply_text(_["yetkikaldırma_2"].format(user.mention))


@app.on_message(
    filters.command(["yetkililiste", "yetkililer"]) & filters.group & ~BANNED_USERS
)
@language
async def yetkililiste(client, message: Message, _):
    _wtf = await get_authuser_names(message.chat.id)
    if not _wtf:
        return await message.reply_text(_["ayarlar_4"])
    else:
        j = 0
        mystic = await message.reply_text(_["yetkililiste_1"])
        text = _["yetkililiste_2"].format(message.chat.title)
        for umm in _wtf:
            _umm = await get_authuser(message.chat.id, umm)
            user_id = _umm["auth_user_id"]
            admin_id = _umm["admin_id"]
            admin_name = _umm["admin_name"]
            try:
                user = (await app.get_users(user_id)).first_name
                j += 1
            except:
                continue
            text += f"{j}➤ {user}[<code>{user_id}</code>]\n"
            text += f"   {_['yetkililiste_3']} {admin_name}[<code>{admin_id}</code>]\n\n"
        await mystic.edit_text(text, reply_markup=close_markup(_))
        

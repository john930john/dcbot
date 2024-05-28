from AnonXMusic import uygulama
from AnonXMusic.utils.veritabanı import c_modunu_al


async def kanal_oynatma_modunu_alCB(_, komut, GeriAramaSorgusu):
    if komut == "c":
        sohbet_id = await c_modunu_al(GeriAramaSorgusu.message.chat.id)
        if sohbet_id is None:
            try:
                return await GeriAramaSorgusu.answer(_["ayar_7"], show_alert=True)
            except:
                return
        try:
            kanal = (await uygulama.get_chat(sohbet_id)).title
        except:
            try:
                return await GeriAramaSorgusu.answer(_["ççal_4"], show_alert=True)
            except:
                return
    else:
        sohbet_id = GeriAramaSorgusu.message.chat.id
        kanal = None
    return sohbet_id, kanal
    

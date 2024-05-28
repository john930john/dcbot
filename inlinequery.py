from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

yanıt = []

yanıt.extend(
    [
        InlineQueryResultArticle(
            title="Duraklat",
            description=f"Geçerli çalan yayını video sohbet üzerinde duraklatır.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Devam",
            description=f"Duraklatılmış yayını video sohbet üzerinde devam ettirir.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Atla",
            description=f"Geçerli çalan yayını video sohbet üzerinde atlar ve bir sonraki yayına geçer.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Son",
            description="Geçerli çalan yayını video sohbet üzerinde sonlandırır.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Karıştır",
            description="Sıradaki şarkıları çalma listesinde karıştırır.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Döngü",
            description="Geçerli çalan şarkıyı video sohbet üzerinde döngüye alır.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)

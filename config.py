import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Bu değeri my.telegram.org/apps adresinden alın.
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Botunuzun kimlik belirtecisini @BotFather üzerinden alın.
BOT_TOKEN = getenv("BOT_TOKEN")

# MongoDB bağlantı URI'sini cloud.mongodb.com adresinden alın.
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400"))

# Botun etkinliklerini kaydetmek için bir grup sohbetinin kimliği.
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Bu değeri @FallenxBot üzerinden /id komutuyla alın.
OWNER_ID = int(getenv("OWNER_ID", 6532412571))

# Heroku'da dağıtıyorsanız bu değişkenleri doldurun.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/mamakli06/mamaklimusic1")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.mamaklibirininruhu")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/mamaklimekani")

# Asistanın otomatik olarak sohbetlerden ayrılmasını istiyorsanız True olarak ayarlayın.
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))

# Spotify'dan API anahtarlarını https://developer.spotify.com/dashboard adresinden alın.
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Youtube, Spotify ve Apple müzik bağlantılarından alınacak maksimum çalma listesi sayısı.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# Telegram ses ve video dosya boyut limiti (byte cinsinden)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))

# Pyrogram v2 oturumları için buradan @StringFatherBot üzerinden alın.
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bazı URL'ler
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/Yeni-11-29")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/Yeni-11-29")
PLAYLIST_IMG_URL = "https://telegra.ph/Eski-11-29"
STATS_IMG_URL = "https://telegra.ph/Eski-11-29"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Eski-11-29"
TELEGRAM_VIDEO_URL = "https://telegra.ph/Eski-11-29"
STREAM_IMG_URL = "https://telegra.ph/Eski-11-29"
SOUNCLOUD_IMG_URL = "https://telegra.ph/Eski-11-29"
YOUTUBE_IMG_URL = "https://telegra.ph/Eski-11-29"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/Eski-11-29"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/Eski-11-29"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/Eski-11-29"


def zaman_dakika_cevir(sure):
    sure_str = str(sure)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(sure_str.split(":"))))


DURATION_LIMIT = int(zaman_dakika_cevir(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(zaman_dakika_cevir(f"{SONG_DOWNLOAD_DURATION}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[HATA] - SUPPORT_CHANNEL URL'niz yanlış. Lütfen https:// ile başladığından emin olun."
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[HATA] - SUPPORT_CHAT URL'niz yanlış. Lütfen https:// ile başladığından emin olun."
        )
        

import json
import subprocess

def okunabilir_zaman(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["saniye", "dakika", "saat", "gün"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

def bytelik_cevir(size: float) -> str:
    """İnsan dostu boyut"""
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        t_n += 1
    return "{:.2f} {}B".format(size, power_dict[t_n])

async def int_alphaya(dizin: int) -> str:
    alfabe = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    metin = ""
    dizin = str(dizin)
    for i in dizin:
        metin += alfabe[int(i)]
    return metin

async def alpha_inte(alfa_dizin: str) -> int:
    alfabe = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    dizin = ""
    for i in alfa_dizin:
        index = alfabe.index(i)
        dizin += str(index)
    dizin = int(dizin)
    return dizin

def zaman_saniyeye(zaman):
    stringt = str(zaman)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

def saniyeden_dakikaya(saniye):
    if saniye is not None:
        saniye = int(saniye)
        g, s, d, s = (
            saniye // (3600 * 24),
            saniye // 3600 % 24,
            saniye % 3600 // 60,
            saniye % 3600 % 60,
        )
        if g > 0:
            return "{:02d}:{:02d}:{:02d}:{:02d}".format(g, s, d, s)
        elif s > 0:
            return "{:02d}:{:02d}:{:02d}".format(s, d, s)
        elif d > 0:
            return "{:02d}:{:02d}".format(d, s)
        elif s > 0:
            return "00:{:02d}".format(s)
    return "-"

def hız_dönüştürücü(saniye, hız):
    if str(hız) == str("0.5"):
        saniye = saniye * 2
    if str(hız) == str("0.75"):
        saniye = saniye + ((50 * saniye) // 100)
    if str(hız) == str("1.5"):
        saniye = saniye - ((25 * saniye) // 100)
    if str(hız) == str("2.0"):
        saniye = saniye - ((50 * saniye) // 100)
    topla = saniye
    if saniye is not None:
        saniye = int(saniye)
        g, s, d, s = (
            saniye // (3600 * 24),
            saniye // 3600 % 24,
            saniye % 3600 // 60,
            saniye % 3600 % 60,
        )
        if g > 0:
            dönüştür = "{:02d}:{:02d}:{:02d}:{:02d}".format(g, s, d, s)
            return dönüştür, topla
        elif s > 0:
            dönüştür = "{:02d}:{:02d}:{:02d}".format(s, d, s)
            return dönüştür, topla
        elif d > 0:
            dönüştür = "{:02d}:{:02d}".format(d, s)
            return dönüştür, topla
        elif s > 0:
            dönüştür = "00:{:02d}".format(s)
            return dönüştür, topla
    return "-"

def süre_kontrolü(dosya_yolu):
    komut = [
        "ffprobe",
        "-loglevel",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        dosya_yolu,
    ]

    pipe = subprocess.Popen(komut, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = pipe.communicate()
    _json = json.loads(out)

    if "format" in _json:
        if "duration" in _json["format"]:
            return float(_json["format"]["duration"])

    if "streams" in _json:
        for s in _json["streams"]:
            if "duration" in s:
                return float(s["duration"])

    return "Bilinmiyor"

formatlar = [
    "webm",
    "mkv",
    "flv",
    "vob",
    "ogv",
    "ogg",
    "rrc",
    "gifv",
    "mng",
    "mov",
    "avi",
    "qt",
    "wmv",
    "yuv",
    "rm",
    "asf",
    "amv",
    "mp4",
    "m4p",
    "m4v",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "m4v",
    "svi",
    "3gp",
    "3g2",
    "mxf",
    "roq",
    "nsv",
    "flv",
    "f4v",
    "f4p",
    "f4a",
    "
              

import os

from ..günlükleme import GÜNCELLEYİCİ


def dizinleri_güncelle():
    for dosya in os.listdir():
        if dosya.endswith(".jpg"):
            os.remove(dosya)
        elif dosya.endswith(".jpeg"):
            os.remove(dosya)
        elif dosya.endswith(".png"):
            os.remove(dosya)

    if "indirilenler" not in os.listdir():
        os.mkdir("indirilenler")
    if "önbellek" not in os.listdir():
        os.mkdir("önbellek")

    GÜNCELLEYİCİ(__name__).bilgi("Dizinler Güncellendi.")
    

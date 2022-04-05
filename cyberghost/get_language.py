import ctypes
import locale

def detect_language():
    windll = ctypes.windll.kernel32
    windll.GetUserDefaultUILanguage()
    lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]

    return lang
#print(lang)
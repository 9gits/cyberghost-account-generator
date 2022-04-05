import pyautogui as pg
import time

from cyber_ghost import search_picture
from get_language import detect_language

def install_control():
    x,y,w,h = search_picture("./picture/install_accept.png")
    pg.click(x+w/2,y+h/2,1)

def install_install(lang):
    print(f"detect language {lang}")
    if lang == "ja_JP" :
        x,y,w,h = search_picture("./picture/install_install.png")
    elif lang == "en_US":
        x,y,w,h = search_picture("./picture/install_install(eng).png")
    else :
        print("input language error")
        exit (-1)
    pg.click(x+w/2,y+h/2,1)

def install_opt():
    x,y,w,h = search_picture("./picture/opt-out.png")
    pg.click(x+w/2,y+h/2,1)


def main_install_control():
    install_control()
    print("click accept")
    time.sleep(20)

    lang = detect_language()
    install_install(lang)
    print("click install")
    time.sleep(20)

    install_opt()
    print("click opt-out")
    time.sleep(20)

#main_install_control()
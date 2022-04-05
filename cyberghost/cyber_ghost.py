# reg_url "https://my.cyberghostvpn.com/ja_JP/signup"
# user/mail //*[@id="email"]　（完全) /html/body/div/div/div/div/div[1]/div/form/div[1]/div/input
# password //*[@id="password_new"]   (完全)　/html/body/div/div/div/div/div[1]/div/form/div[2]/div[1]/input
# re_password //*[@id="password_re"] (完全)　/html/body/div/div/div/div/div[1]/div/form/div[3]/div/input
# signup_btn //*[@id="signup-form"]/div[6]/button (完全)　/html/body/div/div/div/div/div[1]/div/form/div[6]/button


# trial download_url "https://www.cyberghostvpn.com/en_US/vpn-free-trial"
#test_pw z&gK6&8hxG#^!XTauC

from random import random
import pyautogui as pg
import pyperclip as pc
import time

from create_password import get_random_password_string
import global_value as g

#g.mail_address ="testmail"

def click_create():
    """
    i=1.0
    while True:
        if pg.locateOnScreen("./picture/reg.png",confidence=i) == None :
            i-=0.1
            continue
        else :
            x,y,w,h = pg.locateOnScreen("./picture/reg.png",confidence=i)
            pg.click(x+w/2,y+h/2,1)
            break
    """
    x,y,w,h=search_picture("./picture/reg.png")
    pg.click(x+w/2,y+h/2,1)

def input_account(mail):

    x,y,w,h = search_picture("./picture/account.png")


    #input email
    pg.click(x+w/2,y+h/6)
    time.sleep(1)
    pc.copy(g.mail_address)
    pg.hotkey('ctrl','v')
    time.sleep(2)

    #make password
    g.password = get_random_password_string(20)

    #input password
    #pg.click(x+w/2,y+h/6+40)
    pg.press("\t")
    time.sleep(1)
    pc.copy(g.password)
    pg.hotkey('ctrl','v')
    time.sleep(2)

    #input repassword
    #pg.click(x+w/2,y+h/6+80)
    pg.press("\t")
    time.sleep(1)
    pc.copy(g.password)
    pg.hotkey('ctrl','v')
    time.sleep(2)

    print(g.mail_address)
    print(g.password)

    #click sign_up btn
    x,y,w,h = search_picture("./picture/signup.png")
    pg.click(x+w/2,y+h/2,1)

    #(?necessity) wait activate_screen --> misunderstanding resend activation
    time.sleep(30)
    #wait_trial_screen() 

def wait_trial_screen():
    if search_picture("./picture/start_trial.png") == -1:
        x,y,w,h = search_picture("./picture/confirmation required.png")
        #drag
        pg.click(x+w/2,y+10)
        x_move = random(random.randint(-50,50))
        y_move = random(random.randint(-30,30))
        pg.dragRel(x, 0, 3, button='left')
    else :
        x,y,w,h = search_picture("./picture/start_trial.png")
        pg.click(x+w/2,y+h/2)


def search_picture(path):
    i = 1.0
    time_start = time.time()
    time_end = 0
    while True:
        if i <= 0.7:
            i=1.0
            if time_end - time_start > 60 :
                """
                print(f"search_picture {path} error.")
                exit(1)
                """
                return -1
        if pg.locateOnScreen(path,confidence=i) == None :
            i-=0.1
            time_end = time.time()
            continue
        else :
            x,y,w,h = pg.locateOnScreen(path,confidence=i)
            #pg.click(x+w/2,y+h/2,1)
            print(f"confidence:{i}")
            return x,y,w,h
            #break  


def main_cyber_ghost(mail):

    click_create()

    time.sleep(3)

    input_account(mail)
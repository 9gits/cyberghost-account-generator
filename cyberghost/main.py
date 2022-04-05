import time
import undetected_chromedriver.v2 as uc
import os
from os import system

import global_value as g
from mail import confirmation_mail, get_mail_address
from cyber_ghost import main_cyber_ghost
from install_cyber_ghost import main_install_control
from install_exe import install_exefile


path = "./driver/chromedriver.exe"
mail_url = "https://temp-mail.org/?data1=disposableemail_p.2.bestbuytable.cta_t.2_l.en_pid.9441_fpid.6921"
cg_url = ""

#g.mail_address ="testmail"
options = uc.ChromeOptions()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-gpu')

"""
class driver():
    def __init__(self,url,options):
        self.driver = uc.Chrome(executable_path=path,options=options)
        self.driver.get(url)
        return self.driver
"""


def resource_path(relative_path):
    try:
        base_path = system.MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.jopin(base_path,relative_path)
    

def main():
    #install exe
    print("start.")
    #install_exefile()
    time.sleep(10)

    #select language
    #lang = input("PC Language eng or jp>> ")

    #install control
    main_install_control()
    print("control end.")

    #open browser
    #path = resource_path("./driver/chromedriver.exe")
    driver_mail = uc.Chrome(executable_path=path,options=options)
    driver_mail.get(mail_url)
    print("open browser")

    #driver_mail=driver(mail_url,options)

    #get mail_address
    get_mail_address(driver_mail)
    print("get mail_address")

    #control cyber_ghost
    main_cyber_ghost(g.mail_address)
    print("control cyber_ghost_app")

    #check mail
    confirmation_mail(driver_mail)

    #close browser
    driver_mail.close()

if __name__ == '__main__':
    main()

from unicodedata import name
import undetected_chromedriver.v2 as uc
import time

path = "./driver/chromedriver.exe"

options = uc.ChromeOptions()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-gpu')

def main():
    print("screen_shot program.")

    url = input("input url >>")
    picture = input("input screen_shot name >> ")

    #open_browser
    driver = uc.Chrome(path,options=options)
    driver.get(url)
    print("open broser")

    #set_screen
    set_screen(driver)

    #screen_shot
    #driver.save_screenshot(f"./screen_shot/{picture}.png")
    driver.save_screenshot("{picture}.png")
    print("screen shot")

    #close_broser
    driver.close()


def set_screen(driver):
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    print("set screen")
    time.sleep(5)

if __name__ == '__main__' :
    main()
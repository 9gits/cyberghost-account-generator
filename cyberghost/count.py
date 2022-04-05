import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By


path = "./driver/chromedriver.exe"
url = "https://rawmanga.cc/raw-manga/%e3%83%a6%e3%82%a6%e3%82%adhb-%e3%83%8f%e3%83%bc%e3%83%ac%e3%83%a0%e3%81%8d%e3%82%83%e3%82%93%e3%81%b7%e3%81%a3%ef%bc%81-1-2-2/"

#g.mail_address ="testmail"

options = uc.ChromeOptions()
#options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-gpu')




def count(driver):
    count = driver.findElements(By.className("entry_download"))
    print(len(count))

def main_count():

    print("start.")

    driver = uc.Chrome(executable_path=path,options=options)
    driver.get(url)
    #count(driver)

    #count = driver.find_elements(By.className("entry_download"))

    class_name = 'entry_download' 
    count = driver.find_elements_by_class_name(class_name) 

    i = 0
    for elem in count:
        print(elem.text)

    print(i)
    driver.close()


if __name__ == '__main__':
    main_count()
# mail_open btn //*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[3]/div[2]/a
# activate //*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/a (完全)/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/a


# /html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/input


import time

import global_value as g

confirmation_url = "trialstarted?utm_medium=client&utm_source=client_start_trial"

def get_mail_address(driver):
    #get mail-address
    time.sleep(3)
    while True:
        try:
            mail_address_field = driver.find_element_by_xpath('//*[@id="mail"]')
            g.mail_address = mail_address_field.get_attribute('value')
            if "Loading" in g.mail_address :
                #print("Now wait mail address.")
                continue
            else :
                break
        except:
            time.sleep(2)
    #print(g.mail_address)

    #wait
    time.sleep(5)

def confirmation_mail(driver):
    #wait
    time.sleep(5)
    #set screen
    set_screen(driver)

    print("Wait mail")
    
    time_start = time.time()
    time_end = 0

    #open mail
    while True:
        if time_end - time_start > 60 :
            #return -1
            print("open mail time out.")
            exit(1)
        try:
            open_mail_btn = driver.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[3]/div[2]/a')
            driver.save_screenshot("C:/Users/WDAGUtilityAccount/Desktop/open_mail.png")
            open_mail_btn.click()
            break
        except:
            time.sleep(2)
            time_end = time.time()


    #wait
    time.sleep(5)
    print("Check Confirmation btn")
    #set screen
    set_screen(driver)

    time_start = time.time()
    time_end = 0

    #click confirmation-button
    while True:
        if time_end - time_start > 60 :
            #return -1
            print("confirmation time out.")
            exit(1)
        try:
            confirmation_btn = driver.find_element_by_xpath('//*[@id="tm-body"]/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/a')
            driver.save_screenshot("C:/Users/WDAGUtilityAccount/Desktop/confirmation_mail.png")
            confirmation_btn.click()
            break
        except:
            time.sleep(2)
            time_end = time.time()
    
    #print("Confirmation Successful")

    time.sleep(10)
    cur_url = driver.current_url
    print(cur_url)
    #driver.save_screenshot("C:/Users/WDAGUtilityAccount/Desktop/confirmation_homepage.png")
    
    #Test
    """
    while True:
        if confirmation_url in cur_url:
            driver.save_screenshot("C:/Users/WDAGUtilityAccount/Desktop/confirmation_homepage2.png")
            print("confirmation successful")
            break  
    """


def set_screen(driver):
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    print("set screen")
    time.sleep(5)
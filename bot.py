from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import chardet

driver = webdriver.Firefox()
driver.get('http://web.whatsapp.com')
sleep(15)
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div").click()
sleep(5)

fileLocation= "Path/KEYINS.txt"
with open(fileLocation,"r") as file:
    for line in file:
        driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(line)
        driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.ENTER)

sleep(5)

fileLocation= "Path/AESKEY.txt"
with open(fileLocation,"r") as file:
    for line in file:
        driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(line)
        driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.ENTER)
sleep(5)


fileLocation= "Path/AES.txt"
with open(fileLocation,"r") as file:
    for line in file:
        for word in line.split(" "):
            driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(word)
            driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.ENTER)



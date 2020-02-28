from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time

driver =  webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://book.theautomatedtester.co.uk/")
gtitle = driver.title

header = driver.find_element_by_xpath("//div[text()='Selenium: Beginners Guide']")
print(header.text)

links =  driver.find_elements(By.TAG_NAME,"a")
print("Number of links in the Home page is "+ str(len(links)))

for link in links:
    print(link.text)

clickables = driver.find_element(By.LINK_TEXT,"Chapter2")
clickables.click()
time.sleep(2)


driver.close()
sys.exit()

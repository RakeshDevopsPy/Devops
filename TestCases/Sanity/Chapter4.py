from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import alert
import sys
import time

driver =  webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://book.theautomatedtester.co.uk/")
gtitle = driver.title

header = driver.find_element_by_xpath("//div[text()='Selenium: Beginners Guide']")
print(header.text)

driver.find_element_by_link_text('Chapter4').click()
print(driver.title)


Mouse = driver.find_element_by_id("hoverOver")
print(Mouse.text)

MouseOver = ActionChains(driver).move_to_element(driver.find_element_by_id("hoverOver"))
MouseOver.perform()

print(driver.switch_to_alert().text)
driver.switch_to_alert().accept()


time.sleep(5)

driver.close()
sys.exit()

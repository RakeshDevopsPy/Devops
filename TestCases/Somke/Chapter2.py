from selenium import webdriver
from selenium.webdriver import ActionChains
import sys

driver =  webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://book.theautomatedtester.co.uk/")
gtitle = driver.title

header = driver.find_element_by_xpath("//div[text()='Selenium: Beginners Guide']")
print(header.text)


driver.find_element_by_link_text('Chapter2').click()
print(driver.title)

ButtonID = driver.find_element_by_xpath("//input[@value='Button with ID']")
ButtonID.click()

Randombutton = driver.find_element_by_xpath("//div[@id='divontheleft2']/input[2]")
Randombutton.click()

verifybutton =driver.find_element_by_name("verifybutton")
verifybutton.click()

butID = driver.find_element_by_id("but1")
butID.click()

siblingButton = driver.find_element_by_xpath("//input[@id='but1']/following-sibling::input")
siblingButton.click()

chocolatebutton = driver.find_element_by_xpath("//input[@value='chocolate']")
chocolatebutton.click()

driver.find_element_by_link_text('Index').click()

driver.close()
sys.exit()

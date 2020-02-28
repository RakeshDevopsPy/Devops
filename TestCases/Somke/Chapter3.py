from selenium import webdriver
import sys

driver =  webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://book.theautomatedtester.co.uk/")
gtitle = driver.title

driver.find_element_by_link_text('Chapter3').click()
print(driver.title)

virgocancer= driver.find_element_by_xpath("//div[@id = 'divinthecenter']")
print(virgocancer.text)

pool = driver.find_element_by_xpath("//div[@id='leftdiv']")
print(pool.text)

date = driver.find_element_by_xpath("//div[@id='centerdiv']")
print(date.text)

driver.find_element_by_link_text('Index').click()

driver.close()
sys.exit()

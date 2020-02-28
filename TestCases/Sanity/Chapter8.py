from selenium import webdriver
import sys

driver =  webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://book.theautomatedtester.co.uk/")
gtitle = driver.title

header = driver.find_element_by_xpath("//div[text()='Selenium: Beginners Guide']")
print(header.text)

driver.find_element_by_link_text('Chapter8').click()
print(driver.title)

driver.find_element_by_id("secondCookie").click()


driver.close()
sys.exit()

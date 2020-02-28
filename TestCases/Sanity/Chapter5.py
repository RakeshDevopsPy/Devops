import action as action
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)    # implicit wait is not for one single element its for entire webpage
driver.maximize_window()
driver.get("http://book.theautomatedtester.co.uk/")
print("Logged in to Application")
time.sleep(2)
assert driver.page_source.find("Selenium: Beginners Guide")
print("Verified text successfully")
time.sleep(2)
driver.find_element_by_xpath("//div[@class='mainbody']/ul[1]/li[4]/a").click()
driver.find_element_by_xpath(("//div[@id='datediv']/input")).send_keys("Test")
print("Entered text in the text field successfully")
time.sleep(2)
# specific to element use explicit or fleunt wait
selectdropdown=driver.find_element_by_id("selecttype")
if selectdropdown.is_displayed() :
        drp = Select(selectdropdown)
        time.sleep(2)
        drp.select_by_value("Selenium Code")
        time.sleep(2)
        drp.select_by_visible_text(("Selenium RC"))
        time.sleep(2)
        drp.select_by_index("3")
        print("Select the values from dropdown successfully")
else:
        print("unable to find dropdown")
text_alert=driver.find_element_by_id("blurry").send_keys("Happy day")
time.sleep(2)
driver.find_element_by_id("nextBid").click()
time.sleep(2)
alert=driver.switch_to.alert
msg=alert.text
print("Alert shows following message " +msg)
alert.accept()
print("Accepted alert successfully")
time.sleep(2)
action = ActionChains(driver)
Hover = driver.find_element_by_id("hoverOver")
if Hover.is_displayed() :
    action.move_to_element(Hover).perform()
    print("Handover performed successfully")
else:
    print("Handover element not present in this page")
time.sleep(2)
driver.close()
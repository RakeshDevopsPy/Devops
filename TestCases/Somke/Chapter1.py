from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import sys
import time

driver =  webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://book.theautomatedtester.co.uk/")
gtitle = driver.title

header = driver.find_element_by_xpath("//div[text()='Selenium: Beginners Guide']")
print(header.text)

driver.find_element_by_link_text('Chapter1').click()
print(driver.title)

radioButton = driver.find_element_by_id("radiobutton")
if radioButton.is_displayed() and radioButton.is_enabled():
    mousetoRadiobutton= ActionChains(driver).move_to_element(radioButton)
    mousetoRadiobutton.perform()
    radioButton.click()
else:
    print("Unable to identify the radio button")

checkbox = driver.find_element_by_name("selected(1234)")
if checkbox.is_displayed() and checkbox.is_enabled():
    mousetoCheckbox= ActionChains(driver).move_to_element(checkbox)
    mousetoCheckbox.perform()
    checkbox.click()
else:
    print("Unable to identify the check box")

Dropdown = driver.find_element_by_id("selecttype")
if Dropdown.is_enabled() and Dropdown.is_displayed() and checkbox.is_selected():
    drp = Select(Dropdown)
    for x in drp.options:
        print(x.text)
    print("Select by Index")
    drp.select_by_index(1)
    time.sleep(2)
    drp.select_by_index(2)
    time.sleep(2)
    drp.select_by_index(3)
    time.sleep(2)
    print("Select by Value")
    drp.select_by_value("Selenium IDE")
    time.sleep(2)
    drp.select_by_value("Selenium Code")
    time.sleep(2)
    drp.select_by_value("Selenium RC")
    time.sleep(2)
    drp.select_by_value("Selenium Grid")
    time.sleep(2)
    print("Select by visible text")
    drp.select_by_visible_text("Selenium IDE")
    time.sleep(2)
    drp.select_by_visible_text("Selenium Core")
    time.sleep(2)
    drp.select_by_visible_text("Selenium RC")
    time.sleep(2)
    drp.select_by_visible_text("Selenium Grid")

WindowID = driver.current_window_handle
print(WindowID)
window1 = driver. find_element_by_class_name("multiplewindow")
window1.click()
time.sleep(5)
for windows in driver.window_handles:
    if windows != WindowID:
        driver.switch_to_window(windows)
        print(windows)
        driver.close()

driver.switch_to_window(WindowID)
window2 = driver. find_element_by_class_name("multiplewindow2")
window2.click()
time.sleep(5)
for windows in driver.window_handles:
    if windows != WindowID:
        driver.switch_to_window(windows)
        print(windows)
        driver.close()

driver.switch_to_window(WindowID)

driver.close()
sys.exit()


   #for drp in Dropdown:

    #print("All selected Options")
    #drp0 = Select(driver).all_selected_options
    #print(drp0)


# Home_Page = driver.find_element_by_link_text("//a[text()='Home Page']")
#
# hover = ActionChains(driver).move_to_element(Home_Page)
# hover.perform()
# hover.click().perform()
# Home_Page.click()

# password //input[text() = 'Enter your password']
# next button //span[text() = 'Next']

#//span[text()='Confirm']


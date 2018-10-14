import os

Imagepath = os.path.abspath('C:/Users/asus/Whatsapp Automation/test.jpg')
driver.find_element_by_id("Id of the element").clear()
driver.find_element_by_id("Id of the element").send_keys(Imagepath)


elm.send_keys(os.getcwd() + "/test.jpg")


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("your.site.with.dragndrop.functionality.com")
source_element = driver.find_element_by_name('your element to drag')
dest_element = driver.find_element_by_name('element to drag to')
ActionChains(driver).drag_and_drop(source_element, dest_element).perform()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.webdriver.common.action_chains import ActionChains

test_file = open("test.txt", "r+")
num_lines = sum(1 for line in open("test.txt"))
testObj = []

print(num_lines)

for i in range(1, num_lines + 1):
    testObj.append(test_file.readlines(i))

print(testObj)

testObj1 = []
for i in range(0, len(testObj)):
    testObj1.append(testObj[i][0])

t = list(map(lambda s: s.strip(), testObj1))

print(t)
test_file.close()

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
msg = "test message"
count = 1

input("Fuck you all")

for name in t:

    search_user = driver.find_element_by_class_name('jN-F5')
    search_user.send_keys(name, Keys.ENTER)

    # msg_box = driver.find_element_by_class_name('_2bXVy')

    attach = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attach.click()
    attach_file = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/input').send_keys(os.getcwd()+"/test.jpg")
    time.sleep(1)
    ised= driver.find_element_by_class_name('_3nfoJ')
    ised.click()
    time.sleep(0.8)





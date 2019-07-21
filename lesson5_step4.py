import math
from selenium import webdriver

var1 = str(math.ceil(math.pow(math.pi, math.e)*10000))

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

link = browser.find_element_by_link_text(var1)
link.click()

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
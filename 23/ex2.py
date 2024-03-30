from selenium import webdriver
import time
from selenium.webdriver.common.by import By



browser = webdriver.Firefox()
browser.get("https://gmail.com")

username_field = browser.find_element("id","identifierId")
username_field.send_keys("lone08838@gmail.com")



next_btn = browser.find_element_by_class_name("VfPpkd-vQzf8d")
next_btn.click()

# time.sleep(5)



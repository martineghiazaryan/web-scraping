import os
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from selenium.webdriver.common.keys import Keys

# os.environ['PATH'] += r"C:/Users/Admin/Desktop/WebScraping/selenium_simple_automation/selenium_driver"
# driver = webdriver.Chrome()

driver = webdriver.Chrome(executable_path='C:/Users/Admin/Desktop/WebScraping/selenium_simple_automation/selenium_driver')

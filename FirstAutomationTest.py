import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
"""
complete the learning of Selenium(Python) and write the test cases for amazon.com
Learn to automate User Registration and Login 
Learn to automate clicking the slide-over menus with Mouse hover command
Learn to automate scroll action using Mouse Events of Actions class
Learn to automate Search Product
Learn to automate Add to Cart Page
At last we'll learn to automate end-to-end functionality of Buy Product
"""
service = Service(executable_path="C:\\WebDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.amazon.com/")
"""Automate User Registration and Login"""
sign_in_element = driver.find_element(By.ID,"nav-link-accountList-nav-line-1")
action = ActionChains(driver)
action.move_to_element(sign_in_element).click().perform()
driver.find_element(By.ID,"ap_email").send_keys("YOUR_AMAZON_EMAIL_OR_NO")
driver.find_element(By.CLASS_NAME,"a-button-input").click()
driver.find_element(By.ID,"ap_password").send_keys("YOUR_PASSWORD")
driver.find_element(By.ID,"signInSubmit").click()
"""Search Product"""
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("iphone 13")
driver.find_element(By.ID,"nav-search-submit-button").click()
phone_name = driver.find_element(By.LINK_TEXT,"Apple iPhone 11 Pro Max, 256GB, Space Gray - Unlocked (Renewed)")
driver.execute_script("arguments[0].scrollIntoView();",phone_name)
phone.click()
"""Add to Cart Page"""
driver.find_element(By.ID,"add-to-cart-button").click()
driver.find_element(By.NAME,"proceedToRetailCheckout").click()
time.sleep(1)
driver.quit()
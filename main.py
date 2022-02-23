from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

import time

# ------------------------------------ SITE FETCHING -------------------------------------
PATH = "C:/Users/evgenyber/Desktop/python studies/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://instagram.com")
driver.maximize_window
time.sleep(2)

login_with_facebook = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button')
login_with_facebook.click()
time.sleep(1)
facebook_email = driver.find_element_by_name('email')
facebook_email.send_keys('jayber1@gmail.com')
time.sleep(1)
facebook_pass = driver.find_element_by_name('pass')
facebook_pass.send_keys('P304682685p')
time.sleep(1)
fabook_login_button = driver.find_element_by_name('login')
fabook_login_button.click()
time.sleep(10)
not_now = driver.find_element_by_class_name('HoLwm')
not_now.click()
time.sleep(2)
search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('chefsteps')
time.sleep(2)

try:
    search_enter = driver.find_element_by_css_selector('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search_enter.send_keys(Keys.ENTER)
except:
    search_entering = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
    search_entering.click()
time.sleep(2)
followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followers.click()


all_buttons = driver.find_element_by_css_selector("ul li button")
all_buttons.click()
from selenium import webdriver
from getpass import getpass

usr=input('enter the username')
pwd=input('enter the password')

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/')

username_box=driver.find_element_by_id('login-email')
username_box.send_keys(usr)

pawd_box=driver.find_element_by_id('login-password')
pawd_box.send_keys(pwd)

login_btn=driver.find_element_by_id('login-submit')
login_btn.submit()

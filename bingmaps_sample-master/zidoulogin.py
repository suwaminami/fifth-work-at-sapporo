import selenium
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://google.com/')

browser = webdriver.Chrome()
browser.get('https://xxxxx/login_page')
# デプロイした先のURLを記入

elem_username = browser.find_element_by_id('username')
elem_username.send_keys('xxx')
# IDを設定できる

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('xxx')
# PWを設定できる

elem_login_btn = browser.find_element_by_id('login-btn')
elem_login_btn.click()
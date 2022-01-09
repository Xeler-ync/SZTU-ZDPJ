#!/usr/bin/python3
# *coding=utf-8* #

from seleniums import *

import json


def login(driver):
    with open('./xh_pass.json',mode='r',encoding='utf-8') as f: # load xuehao and password
        jsonContent = json.load(f)
    driver.get('https://jwxt.sztu.edu.cn/')
    driver.find_element(By.XPATH,'//*[@id="j_username"]').send_keys(jsonContent['xuehao'])
    driver.find_element(By.XPATH,'//*[@id="j_password"]').send_keys(jsonContent['password'])
    driver.find_element(By.XPATH,'//*[@id="loginButton"]').click()

if __name__ == '__main__':
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    login(driver)
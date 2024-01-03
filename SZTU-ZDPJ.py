#!/usr/bin/python3
# *coding=utf-8* #

import contextlib
from seleniums import *
from systems import *
from login import login

from random import randint
from time import sleep


def evaluate_techer() -> None:
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="Frame1"]'))
    try:
        i = 2
        j = 2
        while 1:
            driver.find_element(By.XPATH,f'//*[@id="table1"]/tbody/tr[{i}]/td[2]/label[{j}]/i').click()
            j = randint(1,2)
            i += 1
    except Exception:
        driver.find_element(By.XPATH,'//*[@id="jynr"]').send_keys('My evaluation')
        try:
            driver.find_element(By.XPATH,'//*[@id="bc"]').click()
            fuck_off_alert()
            fuck_off_alert()
        except Exception:
            driver.find_element(By.XPATH,'//*[@id="qx"]').click()
            fuck_off_alert()

def evaluate_techer_switcher() -> None:
    try:
        i = 2
        while 1:
            driver.find_element(By.XPATH,f'//*[@id="dataList"]/tbody/tr[{i}]/td[8]/a').click()
            evaluate_techer()
            i += 1
    except Exception:
        try:
            driver.find_element(By.XPATH,'//*[@id="btnsubmit"]').click()
        except Exception:
            driver.find_element(By.XPATH,'//*[@id="bc"]').click()
        fuck_off_alert()
        driver.find_element(By.XPATH,'//*[@id="btnShenshen"]').click()
        fuck_off_alert()

def hit_like() -> None:
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="Frame1"]'))
    try:
        i = 2
        while 1:
            driver.find_element(By.XPATH,f'//*[@id="dataList"]/tbody/tr[{i}]/td[7]/a').click()
            fuck_off_alert()
            i += 16
    except Exception:
        driver.find_element(By.XPATH,'//*[@id="btnShenshen"]').click()

def fuck_off_alert() -> None:
    with contextlib.suppress(Exception):
        sleep(1)
        alert = driver.switch_to.alert
        alert.accept()

def select_page() -> None:
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="Frame1"]'))
    driver.find_element(By.XPATH,'//*[@id="Form1"]/table/tbody/tr[4]/td[8]/a').click()
    hit_like()
    driver.find_element(By.XPATH,'//*[@id="Form1"]/table/tbody/tr[2]/td[8]/a').click()
    evaluate_techer_switcher()
    driver.find_element(By.XPATH,'//*[@id="Form1"]/table/tbody/tr[3]/td[8]/a').click()
    evaluate_techer_switcher()
    driver.switch_to.default_content()


def main() -> None:
    global driver, catalog_name, working_catalog_index

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    login(driver)
    sleep(3)
    driver.find_element(By.XPATH,'//*[@id="accordion"]/li[11]/div/i').click()
    driver.find_element(By.XPATH,'//*[@id="accordion"]/li[11]/ul/li/div/i').click()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="accordion"]/li[11]/ul/li/ul/li').click()
    select_page()
    print('Done!')

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

def get_amount():
    MUFG_URL = 'https://entry11.bk.mufg.jp/ibg/dfw/APLIN/loginib/login?_TRANID=AA000_001'

    ID = os.environ['MUFG_ID']
    PASSWORD = os.environ['MUFG_PASSWORD']
    browser = webdriver.PhantomJS()

    try:
        browser.get(MUFG_URL)

        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.ID, 'account_id')
            )
        )

        browser.find_element_by_id('account_id').send_keys(ID)
        browser.find_element_by_id('ib_password').send_keys(PASSWORD)
        # 要素をクリックしたけど効かなかったので、onclickで呼び出している関数を呼び出す
        browser.execute_script('gotoPageFromAA011();')

        WebDriverWait(browser, 3).until(
            expected_conditions.presence_of_element_located(
                (By.ID, 'setAmountDisplay')
            )
        )

        return browser.find_element_by_id('setAmountDisplay').text
    except TimeoutException:
        browser.save_screenshot('debug.png')
        raise
    finally:
        browser.quit()

if __name__ == '__main__':
    print(get_amount())
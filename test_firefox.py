import time

import pytest
from selenium.webdriver.common.by import By

base_url="https://www.instagram.com/"

@pytest.mark.parametrize(("email","FullName","Username","Password","Login","Password2"),
                         [
                             ("Alexandr85@mail.ru","Vladim","Alwsexander0851","123456789",
                              "Alexandr85@mail.ru","3213124142")
                         ])

@pytest.mark.inst
def test_inst_reg(browser_firefox, email, FullName, Username, Password,Login,Password2):
    browser_firefox.get(base_url)
    time.sleep(2)
    browser_firefox.find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > [tabindex='0']:nth-child(2)").click()
    #cookie
    time.sleep(3)
    browser_firefox.find_element(By.CSS_SELECTOR, "._ab25 [dir]").click()
    #Join button
    time.sleep(3)
    browser_firefox.find_element(By.CSS_SELECTOR, "input[name='emailOrPhone']").send_keys(email)
    #email field
    browser_firefox.find_element(By.CSS_SELECTOR, "input[name='fullName']").send_keys(FullName)
    #Name field
    browser_firefox.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(Username)
    #Username field
    browser_firefox.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(Password)
    #Password field
    time.sleep(3)
    browser_firefox.find_element(By.CSS_SELECTOR, "._ab25 > a[role='link']").click()
    #Log in button
    time.sleep(3)
    browser_firefox.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(Login)
    #Login field
    browser_firefox.find_element(By.CSS_SELECTOR, "[method] ._ab32:nth-of-type(2) ._ac4d").send_keys(Password2)
    #Password field
    browser_firefox.find_element(By.CSS_SELECTOR, "._acan._acap._acas._aj1- > .x13lgxp2.x168nmei.x1c4vz4f.x1n2onr6.x1nhvcw1.x1oa3qoh.x1plvlek.x1qjc9v5.x2lah0s.x5pf9jr.x78zum5.x9f619.xdt5ytf.xjbqb8w.xo71vjh.xqjyukv.xryxfnj").click()
    #Log in button
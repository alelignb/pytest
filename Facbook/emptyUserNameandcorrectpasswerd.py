import time
from lib2to3.pgen2 import driver
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from Facbook.loketeor import *
from loginLoketer import *
def test_incoreectun():
    driver = webdriver.Chrome()
    driver.get(web)
    driver.maximize_window()
    time.sleep(1)
    fb_user = driver.find_element(By.NAME, "email")
    fb_user.send_keys()
    time.sleep(1)
    fb_password = driver.find_element(By.NAME, "pass")
    fb_password.send_keys("passwerd124")
    time.sleep(1)
    driver.find_element(By.NAME, "login").click()
    time.sleep(5)
    Error_message = driver.find_element(By.XPATH,
                                        err).text
    assert 'Invalid username or password' == Error_message
    sleep(5)


test_incoreectun()
import time
from lib2to3.pgen2 import driver
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from Facbook.loketeor import *


from loginLoketer import *
def test_login():
    driver = webdriver.Chrome()
    driver.get(web)
    driver.maximize_window()
    time.sleep(1)
    fb_user = driver.find_element(By.NAME, "email")
    fb_user.send_keys("0533984787")
    time.sleep(1)
    fb_password = driver.find_element(By.NAME,"pass")
    fb_password.send_keys("passwerd123")
    time.sleep(1)
    driver.find_element(By.NAME,"login").click()
    time.sleep(25)

test_login()





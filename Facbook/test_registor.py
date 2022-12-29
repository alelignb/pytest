import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from loketeor import *

def test_registor():
    driver = webdriver.Chrome()
    driver.get(facebook_path)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH,
                        registor_path).click()
    time.sleep(3)
    loketerfname = driver.find_element(By.NAME, firstname).send_keys("alelign")
    time.sleep(1)
    loketerlname = driver.find_element(By.NAME, lastname).send_keys("alelign")
    time.sleep(1)
    driver.find_element(By.NAME, email).send_keys("0533984787")

    time.sleep(1)
    pasword = driver.find_element(By.XPATH,paswerd).send_keys("passwerd123")
    time.sleep(1)
    driver.find_element(By.XPATH,mounth).send_keys(
        "october")

    time.sleep(1)

    driver.find_element(By.XPATH, day).send_keys("12")
    time.sleep(1)
    driver.find_element(By.ID, year).send_keys("1988")
    time.sleep(1)

    driver.find_element(By.XPATH,gender).click()
    time.sleep(1)
    signin = driver.find_element(By.XPATH,sinup).click()
    time.sleep(20)


test_registor()

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from atidloketor import *


def test_men():
    driver = webdriver.Chrome()
    driver.get(Atid)
    driver.maximize_window()
    driver.find_element(By.XPATH, home).click()
    sleep(3)
    driver.find_element(By.XPATH, shopKnow).click()
    sleep(3)
    driver.find_element(By.XPATH, ssearch).send_keys("shose")
    sleep(3)
    shooes = driver.find_element(By.XPATH, corsor).click()
    sleep(3)
    assert shooes==h_check



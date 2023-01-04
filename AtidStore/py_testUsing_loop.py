import time
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import select
def test_menu():
    ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.get("https://atid.store")
    time.sleep(3)
    driver.maximize_window()
    menu = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]"
    men = 'li'

    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'STORE':
            n.click()
            break
    driver.implicitly_wait(10)
    pro1 = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[3]/div[1]/a[1]/img[1]"
    driver.find_element(By.XPATH, pro1).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]").click()
    sel = driver.find_element(By.XPATH, "//a[contains(text(),'ATID Blue Shoes')]").text
    assert sel == 'ATID Blue Shoes'
    time.sleep(2)
    driver.execute_script("window.history.go(-3)")
    driver.implicitly_wait(10)
    pro2 = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[7]/div[1]/a[1]/img[1]"
    driver.find_element(By.XPATH, pro2).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]").click()
    sel = driver.find_element(By.XPATH, "//a[contains(text(),'ATID Yellow Shoes')]").text
    assert sel == 'ATID Yellow Shoes'
    time.sleep(2)
    driver.execute_script("window.history.go(-3)")
    driver.implicitly_wait(10)
    pro3 = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[12]/div[1]/a[1]/img[1]"
    driver.find_element(By.XPATH, pro3).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]").click()
    sel = driver.find_element(By.XPATH, "//a[contains(text(),'Blue Denim Shorts')]").text
    assert sel == 'Blue Denim Shorts'
    time.sleep(2)
    driver.execute_script("window.history.go(-4)")
    driver.implicitly_wait(10)
    menu = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'WOMEN':
            n.click()
            break
    driver.implicitly_wait(10)
    pro4 = "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/div[1]/ul[1]/li[8]/div[1]/a[1]/img[1]"
    driver.find_element(By.XPATH, pro4).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]").click()
    sel = driver.find_element(By.XPATH, "//a[contains(text(),'Bright Gold Purse With Chain')]").text
    assert sel == 'Bright Gold Purse With Chain'
    time.sleep(2)
def test_munu1():
    ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.get("https://atid.store")
    time.sleep(3)
    driver.maximize_window()
    menu = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'STORE':
            n.click()
            break
    driver.implicitly_wait(10)
    pro11 = "//span[contains(text(),'Boho Bangle Bracelet')]"
    driver.find_element(By.XPATH, pro11).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,
                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]").click()
    sel = driver.find_element(By.XPATH, "//a[contains(text(),'Boho Bangle Bracelet')]").text
    assert sel == 'Boho Bangle Bracelet'
    time.sleep(2)

def test_cont():
    ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.get("https://atid.store")
    time.sleep(3)
    driver.maximize_window()
    menu = "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]"
    men = 'li'
    me = driver.find_element(By.XPATH, menu)
    m = me.find_elements(By.TAG_NAME, men)
    for n in m:
        if n.text == 'CONTACT US':
            n.click()
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//input[@id='wpforms-15-field_0']").send_keys("belay")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='wpforms-15-field_5']").send_keys("to get coupon code")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='wpforms-15-field_4']").send_keys("belly@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//textarea[@id='wpforms-15-field_2']").send_keys("I need to new coupon code because I wanna be your senior customer")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='wpforms-submit-15']").click()
    time.sleep(2)
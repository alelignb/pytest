from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from atidloketor import *


def test_homeEnd():
    driver = webdriver.Chrome()
    driver.get(Atid)
    driver.maximize_window()
    driver.find_element(By.XPATH, home).click()
    sleep(1)
    driver.find_element(By.XPATH, shopKnow).click()
    sleep(1)
    driver.find_element(By.XPATH,"//h2[contains(text(),'ATID Yellow Shoes')]").click()
    sleep(1)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/button[1]").click()
    sleep(1)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/form[1]/button[1]").click()
    sleep(1)
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]/div[1]/span[1]").click()
    copon= driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys("shose")
    assert copon=="Coupon shous does not exist!"
    sleep(1)

    driver.find_element(By.XPATH, "//button[contains(text(),'Apply coupon')]").click()
    sleep(3)

    driver.find_element(By.XPATH,"//a[contains(text(),'Proceed to checkout')]").click()
    sleep(3)
    driver.find_element(By.XPATH,"//input[@id='billing_first_name']").send_keys("name")
    sleep(1)
    driver.find_element(
        By.XPATH,"//input[@id='billing_last_name']").send_keys("Name")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='billing_company']").send_keys("tech-caree")
    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div[1]/div[1]/div[1]/p[4]/span[1]/span[1]/span[1]/span[1]/span[1]").click()
    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div[1]/div[1]/div[1]/p[4]/span[1]/span[1]/span[1]/span[1]/span[1]").click()
    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div[1]/div[1]/div[1]/p[5]/span[1]/input[1]").send_keys("ZEFAT")
    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div[1]/div[1]/div[1]/p[6]/span[1]/input[1]").send_keys("absorvation center")
    sleep(2)

    driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("12345")
    sleep(2)
    driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys("zefat")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("057654326")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("abdsbgjh@gmail.com")
    sleep(2)
    driver.find_element(By.XPATH,"//button[@id='place_order']").click()
    sleep(2)
    oreder= driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]").click()
    sleep(2)

    assert oreder=="Returning customer? Click here to login"

def test_chekpi0nt():
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


def test_accessorie():
    driver = webdriver.Chrome()
    driver.get(Atid)
    driver.maximize_window()
    sleep(1)
    driver.find_element(By.XPATH,Accsosery).click()

    sleep(1)
    driver.find_element(By.XPATH,select).click()
    sleep(1)
    driver.find_element(By.XPATH,button).click()
    sleep(1)
    driver.find_element(By.XPATH,cartSelect).click()
    sleep(1)
    bank=driver.find_element(By.XPATH,CartAdd).text
    assert bank=="Cart"
    sleep(1)
    coupon_field=driver.find_element(By.XPATH,AmoutSelect)
    coupon_field.clear()
    sleep(1)
    coupon_field.send_keys('dfghjkyu78')
    sleep(1)
    driver.find_element(By.XPATH,"//a[contains(text(),'Proceed to checkout')]").click()
    sleep(2)
    driver.find_element(By.XPATH,"//input[@id='billing_first_name']").send_keys("name")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='billing_last_name']").send_keys("name")
    sleep(2)
    driver.find_element(By.XPATH,"//input[@id='billing_company']" ).send_keys("techcareer")
    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div[1]/div[1]/div[1]/p[4]/span[1]/span[1]/span[1]/span[1]/span[1]" ).click()
    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/span[2]/span[1]/span[2]/ul[1]/li[109]" ).click()
    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div[1]/div[1]/div[1]/p[5]/span[1]/input[1]" ).send_keys("14")

    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div[1]/div[1]/div[1]/p[6]/span[1]/input[1]").send_keys("zefat")
    sleep(2)
    driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("123")
    sleep(2)
    driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys("zefad")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("0586778677")
    sleep(2)
    driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("hgfhmjfvh@gmail.com")
    sleep(2)
    driver.find_element(By.XPATH, "//button[@id='place_order']").click()
    sleep(2)
    chk=driver.find_element(By.XPATH, "//strong[contains(text(),'Billing First name')]").click()
    assert chk =="Billing First name"
    sleep(2)



def test_seche():
    driver = webdriver.Chrome()
    driver.get(Atid)
    driver.maximize_window()
    driver.find_element(By.XPATH , home).click()
    sleep(3)
    driver.find_element(By.XPATH, shopKnow).click()
    sleep(3)
    driver.find_element(By.XPATH, ssearch).click()
    sleep(3)
    driver.find_element(By.XPATH, ssearch).send_keys("shose")
    sleep(3)
    driver.find_element(By.XPATH, filiter).click()
    sleep(3)
    driver.find_element(By.XPATH, h_add).click()
    sleep(3)
    driver.find_element(By.XPATH, h_addtocart).click()
    sleep(3)
    driver.find_element(By.XPATH, h_viewcart).click()
    sleep(3)
    copon=driver.find_element(By.XPATH, cupon).click()
    sleep(3)
    assert copon =="Please enter a coupon code."

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from atidloketor import *


def test_men():
    driver = webdriver.Chrome()
    driver.get(Atid)
    driver.maximize_window()
    driver.find_element(By.XPATH,Mane).click()
    sleep(1)
    driver.find_element(By.XPATH,M_select).click()
    sleep(1)
    driver.find_element(By.NAME,'add-to-cart').click()
    sleep(1)
    driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/a[1]").click()
    sleep(1)
    atanaw=driver.find_element(By.XPATH,"//span[contains(text(),'1')]").text
    sleep(1)
    driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys("thank yuo")
    sleep(1)
    driver.find_element(By.XPATH,"//button[contains(text(),'Apply coupon')]").click()
    sleep(3)

    COP=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]").text
    sleep(1)
    assert COP=='Coupon "thank yuo" does not exist!'

    driver.find_element(By.XPATH,"//button[contains(text(),'Update cart')]").click()
    sleep(1)
    driver.find_element(By.XPATH,"//a[contains(text(),'Proceed to checkout')]").click()
    sleep(1)
    driver.find_element(By.XPATH, "//input[@id='billing_first_name']").send_keys("name")
    sleep(1)
    driver.find_element(By.XPATH, "//input[@id='billing_last_name']").send_keys("name")
    sleep(1)
    driver.find_element(By.XPATH,"//input[@id='billing_company']").send_keys("name")
    sleep(1)
    driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
    sleep(1)
    driver.find_element(By.XPATH,"/html[1]/body[1]/span[2]/span[1]/span[2]/ul[1]/li[110]").click()
    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div[1]/div[1]/div[1]/p[5]/span[1]/input[1]").send_keys("14")
    sleep(2)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/div[1]/div[1]/div[1]/p[6]/span[1]/input[1]").send_keys("zefat")
    sleep(2)
    driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("1234e")
    sleep(2)
    driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys("zefat")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("059878798")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@id='billing_email']").send_keys("awetreyr@gmail.com")
    sleep(2)
    driver.find_element(By.XPATH, "//button[@id='place_order']").click()
    sleep(2)
    BG=driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/ul[1]/li[1]").text
    "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[3]/div[1]/ul[1]/li[1]"
    assert BG=="Billing Postcode / ZIP is not a valid postcode / ZIP."










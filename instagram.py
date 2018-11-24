from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "https://www.instagram.com"
login_url = 'https://www.instagram.com/accounts/login'

driver = webdriver.Chrome('./chromedriver')
ac = ActionChains(driver)
driver.get(login_url)

inputEmail = driver.find_element_by_xpath("//input[contains(@name, 'username')]")
inputEmail.send_keys("01066259880")

inputPass = driver.find_element_by_xpath("//input[contains(@name, 'password')]")
inputPass.send_keys('ab121646')

btn_login = driver.find_element_by_xpath("//button[text()='로그인']")
btn_login.click()

for i in range(2):
    time.sleep(2)
    btn = driver.find_element_by_xpath("//*[text()='나중에 하기']")
    btn.click()

search = "두산"

find = driver.find_element_by_xpath("//input[contains(@placeholder, '검색')]")
find.send_keys('#' + search)

time.sleep(2)
tag = driver.find_elements_by_xpath("//a[contains(@href, '/explore/tags/" + search + "')]")
tag[0].click()

time.sleep(2)
tiles =  driver.find_elements_by_xpath("//*[text()='인기 게시물']/../..//a")

for i in range(len(tiles)):
    tiles[i].click()
    time.sleep(2)
    like = driver.find_element_by_xpath("//*[contains(@aria-label, '좋아요')]")
    like.click()
    close = driver.find_element_by_xpath("//button[text()='닫기']")
    close.click()
    

a = input()
driver.close()

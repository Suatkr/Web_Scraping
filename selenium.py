"""
from selenium import webdriver 
import time 
from selenium.webdriver.common.keys  import Keys


browser= webdriver.Chrome("/Users/Suat KIR/Desktop/chromedriver")

browser.get("https://www.linkedin.com/home")

browser.fullscreen_window()
time.sleep(2)

login= browser.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
time.sleep(3)

email= browser.find_element_by_xpath("//*[@id='username']")

password=browser.find_element_by_xpath("//*[@id='password']")

email.send_keys("ahmetsuat4128@gmail.com")
password.send_keys("2205492314228")

loginbutton=browser.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
loginbutton.click()
time.sleep(1)

search_bar=browser.find_element_by_xpath("//*[@id='global-nav-typeahead']/input")
search_bar.send_keys("#Python")
search_bar.send_keys(Keys.RETURN)

time.sleep(5)



browser.quit()


"""



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time


def get_options():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # For controlling Chrome closing by code (driver.quit())
    return chrome_options


def main():
    chrome_driver_path = "D:\\Development\\chrome_driver\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=get_options())
    driver.maximize_window()
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    time.sleep(50)
    cookie = driver.find_element(By.ID, value="bigCookie")
    while 1 == 1:
        cookie.click()
    # driver.quit()

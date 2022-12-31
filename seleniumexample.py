from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass


def get_options():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # For controlling Chrome closing by code (driver.quit())
    return chrome_options


def main():
    import ShowPassDialog
    parola = ShowPassDialog.main()

    print("Selenium Example")
    chrome_driver_path = "D:\\Development\\chrome_driver\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=get_options())
    driver.maximize_window()
    driver.get("https://www.amazon.com/Casio-MRW200H-1BV-Black-Resin-Watch/dp/B005JVP0LE/?_encoding=UTF8&pd_rd_w"
               "=ipwqC&content-id=amzn1.sym.595f69d1-9647-4ce9-9fca-a43eb1c1f3b6&pf_rd_p=595f69d1-9647-4ce9-9fca"
               "-a43eb1c1f3b6&pf_rd_r=CXNE1ERBEAK8WDSJYEHM&pd_rd_wg=36Ko5&pd_rd_r=693a3af3-a6fe-4407-b5ff"
               "-02cf96de89dd&ref_=pd_gw_exports-popular-this-season-with-similar-asins")
    price_symbol = driver.find_element(By.CLASS_NAME, value="a-price-symbol").text
    price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
    price_decimal = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
    link = driver.find_element(By.XPATH, value='//*[@id="productTitle"]').text
    print(link)
    print("Item price: " + price_symbol + price_whole + "." + price_decimal)
    link_casio_store = driver.find_element(By.XPATH, value='//*[@id="bylineInfo"]')
    link_casio_store.click()
    amazon_search_bar = driver.find_element(By.ID, value='twotabsearchtextbox')
    amazon_search_bar.send_keys("vostok amphibian")
    amazon_search_bar.send_keys(Keys.RETURN)
    amazon_filter_dropdown = driver.find_element(By.XPATH, value='//*[@id="a-autoid-0"]')
    amazon_filter_dropdown.click()
    amazon_filter_dropdown = driver.find_element(By.XPATH, value='//*[@id="s-result-sort-select_2"]')
    amazon_filter_dropdown.click()

    # Signin amazon.com.tr

    driver.get("https://www.amazon.com.tr/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww"
               ".amazon.com.tr%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess"
               "%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_gno_signout&openid.assoc_handle"
               "=trflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    email_txtbox = driver.find_element(By.XPATH, value='//*[@id="ap_email"]')
    email_txtbox.send_keys("suleymangunel@gmail.com")
    email_txtbox.send_keys(Keys.RETURN)
    passwd_txtbox = driver.find_element(By.XPATH, value='//*[@id="ap_password"]')
    passwd_txtbox.send_keys(parola)
    passwd_txtbox.send_keys(Keys.RETURN)
    #driver.quit()

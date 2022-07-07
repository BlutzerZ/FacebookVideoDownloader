from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller


chromedriver_autoinstaller.install() 

def chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") # linux only
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

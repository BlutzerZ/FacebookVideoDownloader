from browser.driver import chrome_driver

if __name__ == "__main__":
    driver = chrome_driver()
    url = str(input("Facebook Url: "))
    driver.get(url)
    
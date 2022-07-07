from selenium import webdriver

def get_element(driver, url):
    driver.get(url)
    ele = driver.page_view
    x = driver.find_elements_by_xpath(f"//*[contains(text(), 'HasteSupportData')]")[-3]
    findFunc = x.split('requireLazy')[-1]
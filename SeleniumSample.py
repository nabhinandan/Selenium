import time

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def test():
    capabilities = webdriver.DesiredCapabilities().FIREFOX
    capabilities["marionette"] = True
    binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities,
                               executable_path="E:/Learning/SeleniumWebdrivers/geckodriver.exe")
    driver.get("https://www.amazon.in/")
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    test()

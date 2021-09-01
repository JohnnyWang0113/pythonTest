from datetime import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.bilibili.com")
driver.implicitly_wait(20)


def xh():
    t = True
    sleep(1)
    while t:
        driver.execute_script("window.scrollBy(0,1000)")
        try:
            driver.find_element('link_text', '没有更多推荐了，返回首页').click()
            sleep(1)
            t = False
        except:
            xh()


driver.quit()

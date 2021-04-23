from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

PATH_TO_DRIVER = "/home/nischay/Development/chromedriver_linux64/chromedriver"
URL = "http://orteil.dashnet.org/experiments/cookie/"


def click_cookie():
    cookie = driver.find_element_by_id("cookie")
    start_time = time.time()
    while True:
        cur_time = time.time()
        if cur_time - start_time > 5:
            buy_upgrade()
            start_time = cur_time
        cookie.click()


def buy_upgrade():
    money = driver.find_element_by_id("money")
    store = driver.find_element_by_id("store")
    store = store.find_elements_by_tag_name("div")
    amount = int(money.text.replace(",", ""))
    # print(amount)
    to_buy = -1

    # buying the first possible item from the end
    for i in range(len(store) - 1, 0, -1):
        item = store[i]
        try:
            text = item.find_element_by_tag_name("b").text
        except NoSuchElementException:
            pass
        else:
            if len(text) > 0:
                value = int((text.split("-")[1]).replace(",", ""))
                # print(value)
                if value <= amount:
                    to_buy = item
                    break
            else:
                pass
    # if item there is any item available to buy
    if type(to_buy) is not int:
        # print(to_buy)
        to_buy.click()


driver = webdriver.Chrome(executable_path=PATH_TO_DRIVER)
driver.get(URL)

click_cookie()

driver.quit()

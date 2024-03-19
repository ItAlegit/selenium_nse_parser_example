from selenium import webdriver
from utilities import (to_viewall, to_most_active, to_main_page, action_init,
                       scroll_to_bot_table, data_parsing, stock_selector)


browser = webdriver.Chrome()
action_init(browser)
browser.get("https://www.nseindia.com/")
# browser.delete_all_cookies()

data_parsing(browser)
# browser.delete_all_cookies()

to_main_page(browser)
# browser.delete_all_cookies()

to_most_active(browser)
# browser.delete_all_cookies()

to_viewall(browser)

stock_selector(browser)
scroll_to_bot_table(browser)

browser.close()

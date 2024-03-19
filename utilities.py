from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time


# создаем глобальную переменную "action", которая будет проинициализирована как ActionChains элемент
def action_init(driver):
    global action
    action = ActionChains(driver)


# функция для сохранения полей "SYMBOL" и "FINAL" после парсинга в файл формата .csv
def save_file(names, total):
    with open("out.csv", "w") as outFile:
        for i in range(len(names)):
            outFile.write(names[i].text + ";" + total[i].text + '\n')


# альтернативная функция прокрутки, аналог driver.scroll_to_element()
# старается скроллить страницу до расположения искомого элемента посередине
def scroll_to_center(driver, element):
    desired_y = (element.size['height'] / 2) + element.location['y']
    window_h = driver.execute_script('return window.innerHeight')
    window_y = driver.execute_script('return window.pageYOffset')
    current_y = (window_h / 2) + window_y
    scroll_y_by = desired_y - current_y
    driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)


# функция парсинга полей "SYMBOL" и "FINAL" с раздела "Pre-Open Market"
def data_parsing(driver):
    # ищем элемент "MARKET DATA", наводится на него для открытия выпадающего меню
    market_data = driver.find_element(By.ID, "link_2")
    action.move_to_element(market_data).perform()
    action.pause(1).perform()
    driver.delete_all_cookies()

    # ищем элемент "Pre-Open Market", кликаем по нему
    preopen_market = driver.find_element(By.LINK_TEXT, "Pre-Open Market")
    action.move_to_element(preopen_market).click().perform()
    action.pause(2).perform()

    # подключаем BeautifulSoup для удобного парсинга
    soup = BeautifulSoup(driver.page_source)
    # процесс парсинга помещен в цикл с проверкой на исключения
    # попытки парсинга будут происходить раз в 2 секунды, пока не будут удачно получены данные
    # сделано это на тот случай, когда страница уже прогружена, но данные таблицы еще не отобразились
    while True:
        try:
            names = soup.find_all(attrs={"class": {"symbol-word-break"}})
            total = soup.find_all(attrs={"class": {"bold text-right"}})
            total.pop(0)
            break
        except:
            time.sleep(2)

    # передаем списки с именами и суммой в функцию сохранения файла
    save_file(names, total)


# переход на главную страницу сайта
def to_main_page(driver):
    # ищем переход на главную страницу, в данном случае ссылка "HOME", переходим
    main_page = driver.find_element(By.ID, value="link_0")
    action.move_to_element(main_page).click()
    action.pause(1).perform()


# клик по элементу "MOST ACTIVE"
def to_most_active(driver):
    # ищем элемент "MOST ACTIVE", располагаем по центру страницы и кликаем по нему
    most_active = driver.find_element(By.ID, value="most_active_tab1")
    scroll_to_center(driver, most_active)
    action.move_to_element(most_active).click().perform()
    action.pause(2).perform()


# клик по элементу "View all"
def to_viewall(driver):
    # ищем элемент со ссылкой "View All", располагаем по центру страницы, переходим
    view_all = driver.find_element(By.LINK_TEXT, value="View All")
    scroll_to_center(driver, view_all)
    action.move_to_element(view_all).click().perform()
    action.pause(2).perform()


# выбор элемента из селектора
def stock_selector(driver):
    # в селекторе выбираем ссылку на список "NIFTY MIDCAP 50"
    selector = Select(driver.find_element(By.ID, "equitieStockSelect"))
    selector.select_by_visible_text("NIFTY MIDCAP 50")
    time.sleep(2)


# прокрутка до нижнего элемента страницы
def scroll_to_bot_table(driver):
    while True:
        try:
            last_element = driver.find_element(By.XPATH, value='//*[@id="equityStockTable"]/tbody/tr[51]/td[1]/a')
            break
        except:
            time.sleep(2)

    scroll_to_center(driver, last_element)
    action.move_to_element(last_element).perform()
    action.pause(2).perform()

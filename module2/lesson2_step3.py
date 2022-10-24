from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math

def sum_2_elem(a, b):
    return str(int(a)+int(b))


try:
    # Открыть страницу
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Найти вводные данные для вычисления 
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    summ = sum_2_elem(x, y)
 
    # Найти селектор и выбрать нужный вариант
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_visible_text(summ)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла

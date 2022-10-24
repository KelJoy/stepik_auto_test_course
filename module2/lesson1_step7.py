import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Найти вводные данные для вычисления и вычислить
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    # Найти поле ввода ответа
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    # Отметить чекбокс
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    # Отметить радиокнопку
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# не забываем оставить пустую строку в конце файла

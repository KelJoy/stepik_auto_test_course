from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://SunInJuly.github.io/execute_script.html"

def func(x):
    return math.log(abs(12*math.sin(int(x))))

try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти вводные данные для вычисления
    x_value = browser.find_element(By.ID,"input_value")

    # Вычислить значение выражения
    result = func(x_value.text)

    # Найти панель ввода результата и отправить результат вычислений
    answer_field = browser.find_element(By.ID,"answer")
    answer_field.send_keys(result)

    # Найти чекбокс, пролистать до него страницу и поставить флажок
    robot_checkbox = browser.find_element(By.ID,"robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    # Отметить радиокнопку
    robot_radio = browser.find_element(By.ID,"robotsRule")
    robot_radio.click()

    # Найти кнопку и отправить ответ
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    # Десятиcекундная пауза
    time.sleep(10)
    # Закрыть браузер
    browser.quit()

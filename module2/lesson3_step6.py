from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Функция для вычисления значения выражения
def func(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"


try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти и нажать на основную кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    # Перейти в новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Найти вводные данные для вычисления
    x_value = browser.find_element(By.ID, "input_value")

    # Вычислить результат
    result = func(x_value.text)

    # Найти поле ввода ответа
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(result)
    
    # Найти кнопку и отправить ответ
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    # Десятиcекундная пауза
    time.sleep(10)
    # Закрыть браузер
    browser.quit()

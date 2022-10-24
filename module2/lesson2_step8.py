from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"


try:
    # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

     # Открыть страницу    
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить поля
    input_first_name = browser.find_element(By.NAME, "firstname")
    input_first_name.send_keys("Hello")
    input_last_name = browser.find_element(By.NAME,"lastname")
    input_last_name.send_keys("World")
    input_email = browser.find_element(By.NAME,"email")
    input_email.send_keys("email@email.ru")

    # Загрузить фаил
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)   
    input_file = browser.find_element(By.NAME, "file")
    input_file.send_keys(file_path)

    
    # Найти кнопку и отправить ответ
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    # Десятиcекундная пауза
    time.sleep(10)
    # Закрыть браузер
    browser.quit()

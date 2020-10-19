from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("1")
    input1 = browser.find_element_by_name("lastname")
    input1.send_keys("1")
    input1 = browser.find_element_by_name("email")
    input1.send_keys("1")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')
    # добавляем к этому пути имя файла 
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

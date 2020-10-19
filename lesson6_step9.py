from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    # Запуск браузера
    browser = webdriver.Chrome()
    browser.get(link)
    # Автозаполнение форм
    input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    input3.send_keys("1@2.ru")
    input4 = browser.find_element_by_css_selector('[placeholder="Input your phone:"]')
    input4.send_keys("123456789")
    input5 = browser.find_element_by_css_selector('[placeholder="Input your address:"]')
    input5.send_keys("1 st, 1-2")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('spec_num', ["895", "896", "897","898", "899", "903", "904", "905"])

def test_start_all_links(browser, spec_num):
    link = f"https://stepik.org/lesson/236{spec_num}/step/1"
    browser.get(link)
    browser.implicitly_wait(20)
    answer = str(math.log(int(time.time())))
    input1 = browser.find_element(By.TAG_NAME, "textarea")
    input1.send_keys(answer)
    
    input2=browser.find_element_by_class_name('submit-submission')
    input2.click()

    input3 = (browser.find_element(By.CLASS_NAME, "smart-hints__hint")).text
    assert input3 == "Correct!", f"Для отчета скопируй: {str(input3)}"
    

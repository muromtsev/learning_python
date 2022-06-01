import math
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")
    browser = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)
    
    browser.get(link)

    x = browser.find_element(By.ID, 'input_value').text
    answer = calc(x)

    inp_area = browser.find_element(By.ID, 'answer')
    inp_area.send_keys(answer)
    time.sleep(3)

    robot = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
    robot.click()
    time.sleep(3)

    robots_rule = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
    robots_rule.click()
    time.sleep(3)

    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.click()


    

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


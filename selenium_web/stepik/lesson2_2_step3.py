import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 

    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 100);")
    valX = browser.find_element(By.ID, "input_value").text
    res = calc(valX)

    
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(res)

    robot = browser.find_element(By.ID, 'robotCheckbox')
    robot.click()

    robotRule = browser.find_element(By.ID, 'robotsRule')
    robotRule.click()
    
    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.click()


    



finally:
    time.sleep(4)
    browser.quit()

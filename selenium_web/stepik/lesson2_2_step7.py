import time, math, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/file_input.html'


try: 

    browser = webdriver.Chrome()
    browser.get(link)
        
    
    name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    name.send_keys('Name')

    name2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    name2.send_keys('Name2')

    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    email.send_keys('email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    elem = browser.find_element(By.ID, "file")
    elem.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn.click()

    



finally:
    time.sleep(4)
    browser.quit()
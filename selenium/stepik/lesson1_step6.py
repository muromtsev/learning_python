from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")
    browser = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=options)
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for idx, element in enumerate(elements):
        element.send_keys(f"Мой ответ {idx}")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
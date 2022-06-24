from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from math import sin, log

def calc(x):
    return str(log(abs(12*sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100')
)


book = browser.find_element(By.ID, "book")
book.click()

x = browser.find_element(By.ID, "input_value").text

answer = calc(x)

field = browser.find_element(By.ID, "answer")
field.send_keys(answer)

btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
btn.click()
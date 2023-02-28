import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

url = 'google.com'

# user_agent = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36

try:
    driver.get(url)

    stock = []
    stock_list = driver.find_element(By.CLASS_NAME, "items_list")
    divs = stock_list.find_elements(By.TAG_NAME, "li")

    for div in divs:
        title = div.find_element(By.CSS_SELECTOR, '.title a').text
        price = div.find_element(By.CLASS_NAME, 'price').text
        stock.append(f"{title}: {price}")

    time.sleep(3)

    with open(file='price.txt', mode='w', encoding='utf=8') as file:
        for elem in stock:
            file.write(f"{elem}\n")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    
    browser.get(link)

    img_treasure = browser.find_element(By.ID, 'treasure')
    valueX = img_treasure.get_attribute('valuex')
    result = calc(valueX)

    answer = browser.find_element(By.ID, 'answer')    
    answer.send_keys(result)

    robot = browser.find_element(By.ID, 'robotCheckbox')
    robot.click()

    robotRule = browser.find_element(By.ID, 'robotsRule')
    robotRule.click()

    
    btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    btn.click()







    # people_radio = browser.find_element(By.ID, "peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # # print("value of people radio: ", people_checked)
    # # assert people_checked is not None, "People radio is not selected by default"
    # # assert people_checked == "true", "People radio is not selected by default"
    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # print("value of robots radio: ", robots_checked)
    # assert robots_checked is None

finally:
    time.sleep(15)
    browser.quit()


import time, math, os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://dota2.fandom.com/wiki/Items'


try: 

    browser = webdriver.Chrome()
    browser.get(link)
    itemLists = browser.find_elements(By.CLASS_NAME, "itemlist")
    elems = itemLists[0].find_elements(By.CSS_SELECTOR, "div")

    for el in elems:
        print(el.get_attribute('title'))
        print(el.get_attribute('href'))
        print('-'*5)
    
    # for el in elems:
    #     print(el.get_attribute('href'))
    #     print(el.get_attribute('title'))
    # with open('items.txt', 'w') as file:
    #     for el in elems:
    #         file.write(el.get_attribute('title'))
    #         file.write(el.get_attribute('href'))
    

    # with open('index.html', 'w') as file:
    #     file.write(browser.page_source)

    
    



finally:
    time.sleep(2)
    browser.quit()
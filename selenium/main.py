from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")
# driver = webdriver.Chrome(executable_path='C:\\Users\\ipozv\\OneDrive\\Рабочий стол\\selenium\\chromedirver\\chromedriver.exe', options=options)
# url = "http://astromebel.ru/"
# user_agent = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
# try:
#     driver.get(url)
    
#     # email_tag = driver.find_element_by_name('email')
#     # password_tag = driver.find_element_by_name('password')
#     # btn_login = driver.find_element_by_id("login-button")

#     # txt = btn_login.text
#     # email_tag.send_keys('123@123.org')
#     # password_tag.send_keys('password123')
#     # btn_login.click()

#     stock = []
#     stock_list = driver.find_element_by_class_name("items_list")
#     divs = stock_list.find_elements_by_class_name("item_wrap")

#     for div in divs:
#         title = div.find_element_by_css_selector('.title a').text
#         price = div.find_element_by_class_name('price').text
#         stock.append((title, price))
        
    
#     time.sleep(5)
    
#     with open(file='price.txt', mode='w') as file:
#         for s in range(len(stock)):
            
#             file.write(f"{stock[s]}\n")
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()







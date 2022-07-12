import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()
reg1 = "http://suninjuly.github.io/registration1.html"
reg2 = "http://suninjuly.github.io/registration2.html"
class TestForm(unittest.TestCase):    

    def isCorrectReg1(self):
        
        browser.get(reg1)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
        
        first_name.send_keys('Test')
        last_name.send_keys('Test')
        email.send_keys('Test')                                

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        return self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Noup!")

    def isCorrectReg2(self):
        
        browser.get(reg2)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")
        
        first_name.send_keys('Test')
        last_name.send_keys('Test')
        email.send_keys('Test')                                

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        return self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Noup!")  

if __name__ == "__main__":
    unittest.main()

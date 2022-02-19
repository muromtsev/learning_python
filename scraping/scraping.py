import requests
from bs4 import BeautifulSoup
import re
# secret_word = 'modules'
# res = requests.get('https://www.w3resource.com/python-exercises/modules/index.php')


# with open('scraping/modeles_page.txt', 'w') as file:
#     file.write(res.text)
# f = ''
with open('scraping/modeles_page.txt', 'r') as file:
    f = file.read()
bs = BeautifulSoup(f, 'html.parser')
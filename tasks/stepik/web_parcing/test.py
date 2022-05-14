# from fake_useragent import UserAgent
# import requests

# URL = 'http://parsinger.ru/task/1/'
# ua = UserAgent()
# headers = {
#     'user-agent': ua.random

# >>> поиск страницы с кодом 200

# for i in range(500, 1, -1):
#     response = requests.get(url=f"{URL}{i}.html")
#     if response.status_code == 200:
#         print(f"Номер ссылки: {i} status => {response.status_code}")
#         break
#     else:
        
#         print(f"Номер ссылки: {i} status => {response.status_code}")
#         continue

# >>> download image

# response = requests.get(url='http://httpbin.org/image/jpeg')
# with open('image.jpeg', 'wb') as file:
#     file.write(response.content)


# from bs4 import BeautifulSoup
# import requests
# import lxml

# response = requests.get(url='http://parsinger.ru/html/hdd/4/4_1.html')
# response.encoding='utf-8'
# bs = BeautifulSoup(response.text, 'lxml')

# prices = [x.text for x in bs.find_all('p', class_='price')]

# nums = [x.replace(' руб', '') for x in prices]

# def func(list_):
#     sum = 0
#     for i in list_:
#         sum += int(i)
#     return sum

# price = bs.find('span', id='price').text
# old_price = bs.find('span', id='old_price').text
# new = int(price.replace(' руб', ''))
# old = int(old_price.replace(' руб', ''))
# print(new, old)
# sale = (old - new) * 100 / old
# print(sale)


# from bs4 import BeautifulSoup
# import requests

# url = 'http://parsinger.ru/html/index3_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# shema = 'http://parsinger.ru/html/'
# pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]


# list_list_name = list()
# for page in range(1, int(pagen) + 1):
#     url = f'http://parsinger.ru/html/index3_page_{page}.html'
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     print(f">>>PAGE: {page}..")
#     list_name_item = [link.text for link in soup.find_all('a', class_='name_item')]
#     print(f"[FINISH]: {page}..")
#     list_list_name.append(list_name_item)
# print("[COMPLETE!!!]")


# from bs4 import BeautifulSoup
# import requests

# sum = 0
# for page in range(1, 5):
#     url = f'http://parsinger.ru/html/index3_page_{page}.html'
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     print(f">>> PAGE: {page}")
#     soup = BeautifulSoup(response.text, 'lxml')
#     links = [link['href'] for link in soup.find_all('a', class_='name_item')]

#     for sub_link in links:
#         url = f'http://parsinger.ru/html/{sub_link}'
#         response = requests.get(url=url)
#         response.encoding = 'utf-8'
#         print(f"URL: {url}")
#         soup = BeautifulSoup(response.text, 'lxml')
#         article = soup.find('p', class_='article').text
#         article_number = article.replace('Артикул: ', '')
#         print(f"ARTICLE: {article_number}")
#         print('*'*30)
#         print('\n')
#         sum += int(article_number)

# print(f"Общая сумма артиклов: {sum}")

from bs4 import BeautifulSoup
import requests
import time

multi, result = 0, 0

for menu_link in range(1, 6):
    
    print(f"Number link: {menu_link}")

    for page in range(1, 5):
        url = f"http://parsinger.ru/html/index{menu_link}_page_{page}.html"
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        links = [link['href'] for link in soup.find_all('a', class_='name_item')]
        
        time.sleep(2)

        for sub_link in links:
            url = f'http://parsinger.ru/html/{sub_link}'
            response = requests.get(url=url)
            response.encoding = 'utf-8'
            print(f"URL: {url}")
            soup = BeautifulSoup(response.text, 'lxml')
            total_span = soup.find('span', id='in_stock').text
            price_span = soup.find('span', id='price').text

            total = total_span.replace('В наличии: ', '')
            price = price_span.replace(' руб', '')
            print()
            print(f"TOTAL: {total} PRICE: {price}")
            multi = int(total) * int(price)
            result += multi
            print()
            print(f"RESULT: {result}")
            
            time.sleep(2)
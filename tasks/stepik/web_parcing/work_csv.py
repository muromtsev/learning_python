import csv
import requests
from bs4 import BeautifulSoup

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Наименование', 'Бренд', 'Форм-фактор,', 'Ёмкость', 'Объём буф. памяти', 'Цена'])

for page in range(1, 5):
    url = f'http://parsinger.ru/html/index4_page_{page}.html'

    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]
    print(description)
    for item, price, descr in zip(name, price, description):
        result = []
        flatten = item, [x.split(':')[1].strip() for x in descr if x], price

        for x in flatten:
            if isinstance(x, list):
                for i in x:
                    result.append(i)
            else:
                result.append(x)
        print(result)

        with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(result)
    print('Файл res.csv создан')
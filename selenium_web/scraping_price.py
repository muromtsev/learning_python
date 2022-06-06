from bs4 import BeautifulSoup
import json

def get_items_url(url):
    for i in range(1, 4):

        with open(f'selenium/divany-{i}.html') as file:
            src = file.read()
    
        soup = BeautifulSoup(src, "html.parser")
        items = soup.select(".items_list li")
        dict_data = []
        
        for elem in items:
            title = elem.find('h3')
            link = title.find('a').get('href')
            name = title.get_text().strip()
            price = elem.find('div', 'price').get_text().strip()
            dict_data.append(
                {
                    "name": name,
                    "URL": f'{url}{link}',
                    "price": price[3:-5]
                    
                }
            )
        with open(f'selenium/price-{i}.json', 'w') as file:
            json.dump(dict_data, file, indent=4, ensure_ascii=False)

# get_items_url()


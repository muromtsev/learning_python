import json
from turtle import width
from bs4 import BeautifulSoup
import re

with open('./items.html') as file:
    page = file.read()

URL = 'https://dota2.fandom.com/'

bs = BeautifulSoup(page, 'html.parser')
# titles h2[1-5]
h2 = bs.select('h2 > span')

#titles h3
h3 = bs.select('h3 > span')

items_list = bs.select('.itemlist div > a:first-child')

#image => (items_list[1].next_element.get('data-src'))

dict_items = {}

for idx, item in enumerate(items_list):
    name = item.get('title')

    rename = re.sub('\([^()]+\)', '', name)
    search_coast = re.findall(r'\d+', name)
    if search_coast:
        coast = search_coast[0]
    else:
        coast = '0'

    item_url = item.get('href')
    item_img = item.next_element
    w = item_img.get('width')
    h = item_img.get('height')
    item_img_url = item_img.get('data-src')
    
    dict_items[rename] = rename.strip()
    dict_items[rename] = dict(id=idx, coast=coast, URL=item_url, image_url=item_img_url, width=w, height=h)

with open('dict_items.json', 'w') as file:
    json.dump(dict_items, file, indent=4, ensure_ascii=False)

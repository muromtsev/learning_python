import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import datetime
import random
import json

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

def get_source_html(search_word='bosch'):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")

    driver = webdriver.Chrome(executable_path='C:\\Users\\ipozv\\OneDrive\\Рабочий стол\\learning_python\\selenium\\chromedriver\\chromedriver.exe', options=options)
    driver.maximize_window()
    url = f"https://www.avito.ru/volgograd/remont_i_stroitelstvo/instrumenty-ASgBAgICAURYoks?cd=1&q={search_word}"


    try:
        driver.get(url)
        time.sleep(5)

        with open(f"selenium/{search_word}.html", "w") as file:
            file.write(driver.page_source)
    
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def get_items_url(file_path):
    now = datetime.datetime.now()
    date_now = now.strftime("%d-%m-%Y")
    with open(file_path) as file:
        src = file.read()
    
    soup = BeautifulSoup(src, "html.parser")
    items_a = soup.find_all(attrs={"data-marker": "item-title"})

    urls = []

    for item in items_a:
        link = item.get("href")
        urls.append(link)

    with open(f'selenium/links-{date_now}.txt', 'w') as file:
        for url in urls:
            file.write(f"https://www.avito.ru/{url}\n")
    return "[INFO] COMPLETE!"

def get_data(file_path):
    with open(file_path) as file:
        urls_list = [url.strip() for url in file.readlines()]

    result_list = []
    urls_count = len(urls_list)
    count = 1

    for url in urls_list:
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            item_metadata = soup.find('div', class_='title-info-metadata-item-redesign').text.strip()
        except Exception as ex:
            item_metadata = None
        try: 
            item_name = soup.find('span', class_='title-info-title-text').text.strip()
        except Exception as ex:
            item_name = None
        try: 
            item_price = soup.find('span', class_='js-item-price').text.strip()
        except Exception as ex:
            item_price = None
        try: 
            item_params = soup.find_all('li', class_='item-params-list-item')
            item_brand = item_params[2].text.strip()
            item_condition = item_params[1].text.strip()
        except Exception as ex:
            item_params = None
            item_brand = None
            item_condition = None
        try: 
            item_address = soup.find('span', class_='item-address__string').text.strip()
        except Exception as ex:
            item_address = None
        try: 
            item_descr = soup.find('div', class_='item-description-text').text.strip()
        except Exception as ex:
            item_descr = None
        result_list.append(
            {
                "Name": item_name,
                "Date": item_metadata,
                "URL": url,
                "Price": item_price,
                "Brand": item_brand,
                "Condition": item_condition,
                "Address": item_address,
                "Description": item_descr
            }
        )
        time.sleep(random.randrange(2, 5))

        if count % 10 == 0:
            time.sleep(random.randrange(3, 6))

        print(f"[.] Processed: {count}/{urls_count}")

        count += 1

    with open('learning_python/selenium/result.json', 'w') as file:
        json.dump(result_list, file, indent=4, ensure_ascii=False)

    return "[INFO] COMPLETE!"

def set_links(file_path):
    with open(file_path) as file:
        urls_set = {url.strip() for url in file.readlines()}
    return urls_set


def main():
    # get_source_html(search_word='prebena')
    # print(get_items_url('selenium/prebena.html'))
    # print(get_data('learning_python/selenium/links.txt'))
    old_set = set_links('selenium/links.txt')
    now_set = set_links('selenium/links-15-03-2022.txt')
    print(len(old_set))
    print(len(now_set))
    
    print(old_set.difference(now_set))

if __name__ == '__main__':
    main()

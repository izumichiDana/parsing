# Web Scraping - 
# Web Crowling - pauki kotorye lazyiut po saitam i ishut dannye
# Web Parsing - poluchenie i obrabotka dannyh

# "hello    ".strip()



# # virtual



# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint 


# response = requests.get("https://www.kivano.kg/elektronika")
# print(response)


# # print(response.status_code)
# # print(response.url)
# # print(response.headers)
# # print(response.cookies)
# # print(response.content)
# # pprint(response.text)






# import requests
# from bs4 import BeautifulSoup

# def get_html(url):
#     response = requests.get(url)
#     return response.text


# def get_links(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     print(soup.find("a").get("href"))


# url = "https://kivano.kg/elektronika"

# html = get_html(url)
# links = get_links(html)




"""""helpers.py naastin kod"""

# from bs4 import BeautifulSoup


# def get_attr_value(tag, attr):
#     """Получает тег и по аттрибуту
#     возвращает значение:
#     <a href="/product/view/karta-pamyati-micro-sd-apacer-hc10-u3-v30-256gb"
#     target="_blank">
#     get_attr_value(tag, "href") -> /link/
#     """
#     from scraping_page import BASE_URL
#     return BASE_URL + tag.get(attr)


# def get_tags(ls_soup, tag_name, attrs=None):
#     find_tags = []
#     for tag in ls_soup:
#         res = tag.find(tag_name, attrs)
#         find_tags.append(res.get("href"))
#     # ["/product/sadasd/", "/product/sadasd/"]
#     return find_tags


# def is_disabled(html):
#     """Вернет True, когда мы дойдем до конца"""
    
#     soup = BeautifulSoup(html, 'html.parser')
#     li_obj = soup.find('li', attrs={'class': 'next'})
#     # next disabled
#     if 'disabled' in li_obj.get('class'):
#         return True
#     return False



"""""main.py nastin kod"""

# from scraping_page import get_all_links, BASE_URL
# from scraping_details import get_item_details
# import json

# def main():
#     products = []

#     # получаем ссылки на все продукты со всех страниц
#     all_products_links = get_all_links()

#     for product_url in all_products_links:
#         # получаем данные по каждому продукту и добавляем в список
#         product_details = get_item_details(BASE_URL + product_url)
#         products.append(product_details)

#     with open("db.json", "w", encoding='utf-8') as file:
#         # записываем полученный список с информацией о продуктах в файл
#         json.dump(products, file, ensure_ascii=False)

# if __name__ == '__main__':
#     main()


"""""scraping_ditails.py nastin kod"""


# # название
# # описание
# # цена
# # фотка

# from scraping_page import get_html
# from bs4 import BeautifulSoup

# def get_item_details(url:str) -> dict:
#     data = {}
#     html = get_html(url)
#     soup = BeautifulSoup(html, "html.parser")

#     # ищем title
#     title = soup.find('h1').text
#     data['title'] = title

#     # ищем описание
#     desc_div = soup.find("div", {"class":"shop_text"})
#     desc = desc_div.find("span", {"itemprop":"description"}).text
#     data["description"] = desc

#     # ищем цену
#     price = soup.find("span", {"itemprop":"price"}).text.strip()
#     data['price'] = price

#     # ищем фотку
#     img_div = soup.find("div", {"class":"img_full"})
#     img = img_div.find("img").get("content")
#     data['photo'] = img

#     return data



"""""scraping_page.py nastin kod"""



# import time

# import requests
# from bs4 import BeautifulSoup
# from helpers import get_tags, is_disabled

# # find - return soup object
# # find_all() - return list(python list) of find object


# BASE_URL = "https://enter.kg/web-kamery_bishkek"

# def get_last_page():
#     html = get_html(BASE_URL + '/web-kamery_bishkek')
#     soup = BeautifulSoup(html, "html.parser")
#     last_page = soup.find("div", {"class":"row"}).text
#     return last_page


# def get_html(url):
#     """Получает ссылку и возвращает
#     его структуру html ввиде текста
#     """
#     response = requests.get(url)
#     return response.text


# def get_links(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     product_links_container = soup.find('div', attrs={'class': 'row'})
#     res = product_links_container.find_all('div', attrs={'class': 'product vm-col vm-col-1'})
#     list_of_a = get_tags(res, 'a', attrs={})
#     return list_of_a


# def get_all_links():
#     all_links = []
#     # находим номер последней страницы
#     last_page = get_last_page()
#     url = BASE_URL + "/web-kamery_bishkek?page={}"
#     # проходимся по каждой странице
#     for page in range(116, int(last_page)+1):
#         print(page)
#         html = get_html(url.format(page))
#         # добавляем в список новые ссылки на продукты
#         all_links += get_links(html)

#     return all_links


# if __name__ == '__main__':
#     print(get_all_links())






import requests
from bs4 import BeautifulSoup
import csv

HOST = 'https://kg.wildberries.ru'
URL = 'https://kg.wildberries.ru/catalog/elektronika/krasota-i-zdorove'
HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r.text

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='product-card')
    cards = []
    for item in items:
        cards.append(
            {
                'title':item.find('div', class_='product-card__brand-name').get_text(strip=True),
                'price':item.find('span', class_='price').get_text(strip=True),
            }
        )
    print(cards)
html = get_html(URL)
get_content(html)



"""""chto to hz"""

# def get_total_pages(html):
#     soup = BS(html, 'lxml')
#     pages_ul = soup.find("div", class_='vm-pagination vm-pagination-bottom').find('ul')
#     last_page = pages_ul.find('li')
#     # total_pages = last_page.find_all('a').get('href').split('=')[-1]
#     return pages_ul

# def get_page_data(html):
#     soup = BS(html, 'lxml')
#     product_list = soup.find_all('div', class_='row').find('div', class_='product vm-col vm-col-1')
#     print(product_list)
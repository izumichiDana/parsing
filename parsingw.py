from bs4 import BeautifulSoup
import requests
import lxml

def get_html(monitory_url):
    answer = requests.get(monitory_url)
    return answer.text

def get_product_data(html):
    product_list_name = []
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find_all('div', class_='row')
    for product in products:
        x = product.find('div', class_='row').find('a').text
        product_list_name.append(x)
    print(product_list_name)


def get_product_data(product_list):
    soup = BeautifulSoup(product_list, 'lxml')
    product_list2 = []
    products = soup.find_all('div', class_='row')
    for product in products:
        x = product.find('a').get('href')
        product_list2.append(x)
    return product_list2

def main():
    monitory_url = 'https://enter.kg/monitory_bishkek'
    get_product_data(get_html(monitory_url))

main()

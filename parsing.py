import requests
from bs4 import BeautifulSoup as BS
import csv 



def get_html(url):
    response = requests.get(url)
    return response.text


def write_to_csv(data):
    with open("enter_kg.csv", 'w') as file1:
        writer = csv.writer(file1, delimiter='/')
        writer.writerow((data['title'],
                        data['price'],
                        data['img']))


def get_product_data(html):
    soup = BS(html, 'lxml')
    products = soup.find_all('div', class_='row')


    for product in products:
        img = product.find('a').find('img').get('src')
        title = product.find('div', class_ = 'rows').find('a').text
        price = product.find('span', class_ = 'price').text
    
        data = {'title': title, 'price': price, 'img': img} 
        print(data)



# def write_to_csv(data):
#     with open("enter_kg.csv", 'a') as file1:
#         writer = csv.writer(file1, delimiter='/')
#         writer.writerow((data['title'],
#                         data['price'],
#                         data['img']))
   

def main():
    pitanie = 'https://enter.kg/monitory_bishkek'
    get_product_data(get_html(pitanie))


main()
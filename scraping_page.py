import time
import requests
from bs4 import BeautifulSoup
from helpers import get_attr_value, get_tags, is_disablebled

BASE_URL = "https://www.kivano.kg"

def get_html(url):

    sleep = 1 
    while True:
        try:
            response = requests.get(url)
            return response.text
        except Exception as e:
            print(f'Error Http Connection and time sleep {sleep} seconds')
            time.sleep(sleep)
            sleep += 3


def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_links_conteiner = soup.find('div', attrs={'class': 'list-view'})
    res = product_links_conteiner.find_all('div', attrs={'class':'listbox_title'})
    list_of_a = get_tags(res, 'a', attrs={})
    return list_of_a


def get_all_links():
    all_links =[]
    status = True
    count = 1
    while status:
        url = BASE_URL + "elektronika?page={}"
        html = get_html(url.format(count))
        print(url.format(count))
        all_links.append(get_links(html))
        count +=1
        if is_disablebled(html):
            break
    return all_links

if __name__ == '__main__':
    print(get_all_links())


url = "https://kivano.kg/elektronika"



# def main():
#     html = get_html(BASE_URL)



# links = get_links(html)



# import requests
# from bs4 import BeautifulSoup
# from helpers import get_attr_value, get_tags
# # find - return soup object
# # find_all - return list(python list) of find object


# def get_html(url):
# # poluchaet ssylku i vozvrawaet ego strukturu html v vide texta
#     response = requests.get(url)
#     return response.text


# def get_links(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     product_links_container = soup.find('div', attrs={'class': 'list-view'})
#     res = product_links_container.find_all('div', attrs={'class': 'listbox_title'})
#     list_of_a = get_tags(res, 'a', attrs={})
#     print(list_of_a)

# url = "https://www.kivano.kg/elektronika"
# html = get_html(url)
# links = get_links(html)










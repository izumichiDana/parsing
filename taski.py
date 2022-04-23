# task 1
# import requests
# source = requests.put('https://stackoverflow.com/questions').status_code
# print(source)



# text - еще один встроенный метод объектов requests, который возвратит нам информацию в текстовом формате:

# access = requests.get(http://neopythonic.blogspot.com/).text
# print(access) 
# soup = BeautifulSoup(access, 'lxml')
# print(soup)




# one_post = soup.find('div', 'date-outer')
# print(one_post)


"""kod Janbolota"""""
# import requests
# from bs4 import BeautifulSoup
# import lxml
# source = requests.get('http://www.example.com/').text
# my_page = BeautifulSoup(source, 'lxml')
# print('h1: ', my_page.h1.text)
# print('p: ', my_page.p.text)
# print('a: ', my_page.find('a').get('href'))

"""to sto ya pytalas sama sdelat"""
# import requests 
# from bs4 import BeautifulSoup
# import lxml
# sours = requests.get('http://www.example.com/').text
# my_page = BeautifulSoup(sours,'lxml')
# print('h1: ', my_page.h1.text)
# print('p: ', my_page.p.text)
# print('a: ', my_page.find('a').get('href'))


"""shto to nachinayu ponimat"""
# import requests 
# from bs4 import BeautifulSoup
# import lxml
# sours = requests.get('https://www.wikipedia.org/').text
# my_page = BeautifulSoup(sours,'lxml')

# res = my_page.find(id="js-link-box-de")
# print(res.strong.text)
# print(res.small.text)




""""kod Raxata"""
# import requests 
# from bs4 import BeautifulSoup

# def getTitle(url):
#     link = requests.get(url).text
#     try:
#         return f"'h1: ', {link.h1.text}"
#     except Exeception as e:
#         raise 'Title could not be found'

# print(getTitle('http://www.example.com/'))



"""""moi spijennyi kod ot koda janbolota"""
# import requests
# from bs4 import BeautifulSoup
# def getTitle(url):
#     source = requests.get(url).text
#     soup = BeautifulSoup(source, 'lxml')
#     if soup.h1:
#         return soup.h1
#     else:
#         return 'Title could not be found'

# print(getTitle('http://www.example.com/'))


"""""sto to na tatarskom"""

# import requests 
# from bs4 import BeautifulSoup
# soup = requests.get('https://www.makers.kg').text
# t = BeautifulSoup(soup, 'lxml')
# res = t.find_all('h3', 'feature-cards-card-info-title')
# for x in res:
#     print(x.text)



"""""task parsing"""

# goods-card__container  prigoditsa

#row 



from bs4 import BeautifulSoup



def get_attr_value(tag, attr):
# poluchaet tag i po atributu vozvrawaet znachenie
# def get_attr_value(tag, "href"): -> /link/
    return tag.get(attr)

    from scraping_page import BASE_URL
    return BASE_URL + tag.get(attr)



def is_disablebled(html):
    soup = BeautifulSoup(html, 'html.parser')
    li_ibj = soup.find('li', attrs={'class': 'next'})
    if 'disabled' in li_ibj.get('class'):
        return True
    return False

def get_tags(ls_soup, tag_name, attrs):
    find_tags = []
    for tag in ls_soup:
        res = tag.find(tag_name, attrs)
        # res = get_attr_value(tag, 'href')
        find_tags.append(get_attr_value(res, 'href'))
    return find_tags


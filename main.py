import requests
from bs4 import BeautifulSoup

def scrap():
    page = requests.get(
        'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=graphics+card&_sacat=0').text
    soup = BeautifulSoup(page, 'lxml')
    art = soup.find_all('li', class_='s-item s-item__pl-on-bottom s-item--watch-at-corner')

    for x in art:
        try:
            name = x.find('h3', class_='s-item__title').text
            price = x.find('div', class_='s-item__detail s-item__detail--primary').text
            shipping = x.find('span', class_='s-item__shipping s-item__logisticsCost').text
            origin_country = x.find('span', class_='s-item__location s-item__itemLocation').text
            prod_link = x.find('a')['href']
            con = x.find('div', class_='s-item__subtitle').text.split('·')
            condition, brand_name, model_name, gpx_mem = con[0], con[1], con[2], con[3]

            print(brand_name, condition, model_name, gpx_mem, price, shipping, origin_country, prod_link)

        except:
            pass


if __name__ == '__main__':
    scrap()



import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
s = simpledialog.askinteger(title="Page", prompt="How many pages do you need from Ebay?:")


def scrap():
    # creates a file named eBay_graphics_card and writes the collected data as .csv
    with open('eBay_graphics_card.csv', 'w', newline='') as out:
        _writer = csv.writer(out)
        # writes header as first object in the file
        _writer.writerow(['NAME IN SITE', 'BRAND', 'CONDITION', 'MODEL NAME', 'GRAPHICS MEMORY',
                          'PRICE', 'ORIGIN COUNTRY', 'SHIPPING', 'LINK'])

        for i in range(s):
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                    ' Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
            page = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_nkw=graphics+card&_sacat=0&_pgn={i}',
            headers=header).text
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

                    _writer.writerow([name, brand_name, condition, model_name, gpx_mem, price, origin_country,
                                      shipping, prod_link])

                except:
                    pass


if __name__ == '__main__':
    scrap()



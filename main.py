import csv
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import simpledialog
from time import sleep

ROOT = tk.Tk()

ROOT.withdraw()
# item input
item = simpledialog.askstring(title='Item', prompt='What item are you looking for?')

ROOT = tk.Tk()

ROOT.withdraw()
# page(s) input
s = simpledialog.askinteger(title="Page", prompt="How many pages do you need from Ebay?")


def scrap():
    # creates a file named eBay_scrapper and writes the collected data as .csv
    with open('eBay_scrapper.csv', 'w', newline='') as out:
        _writer = csv.writer(out)
        # writes header as first object in the file
        _writer.writerow(['NAME IN SITE', 'CONDITION', 'PRICE', 'SHIPPING', 'LINK'])

        for i in range(s):
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                    ' Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
            page = requests.get(
                f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={item}&_sacat=0&LH_TitleDesc=0&_pgn={i}',
                headers=header).text
            sleep(2)
            soup = BeautifulSoup(page, 'lxml')
            art = soup.find_all('li', class_=['s-item s-item__pl-on-bottom s-item--watch-at-corner',
                                              's-item s-item__pl-on-bottom',
                                              's-item s-item__pl-on-bottom s-item--watch-at-corner s-item__before-answer'])
            tar = soup.find_all('li', class_=['s-item s-item__pl-on-bottom',
                                              's-item s-item__pl-on-bottom s-item--watch-at-corner',
                                              's-item s-item__pl-on-bottom s-item--watch-at-corner s-item__before-answer'])

            # eBay section using 'art' as class
            for x in art:
                try:
                    name = x.find('h3', class_='s-item__title').text
                    price = x.find('div', class_='s-item__detail s-item__detail--primary').text
                    shipping = x.find('span', class_='s-item__shipping s-item__logisticsCost').text
                    prod_link = x.find('a')['href']
                    con = x.find('div', class_='s-item__subtitle').text.split('·')
                    condition, brand_name, model_name, gpx_mem = con[0], con[1], con[2], con[3]

                    _writer.writerow([name, condition, price, shipping, prod_link])

                except:
                    pass

            # eBay section using 'tar' as class
            for n in tar:
                try:
                    name = n.find('h3', class_='s-item__title').text
                    state = n.find('span', class_='SECONDARY_INFO').text
                    prc = n.find('span', class_='s-item__price').text
                    shp = n.find('span', class_='s-item__shipping s-item__logisticsCost').text
                    link = n.find('a')['href']

                    _writer.writerow([name, state, prc, shp, link])

                except:
                    pass
    return _writer


if __name__ == '__main__':
    scrap()



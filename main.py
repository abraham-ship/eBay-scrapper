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

            # look for particular elements describing product
            for x in art:
                try:
                    name = x.find('h3', class_='s-item__title').text
                    state = x.find('span', class_='SECONDARY_INFO').text
                    prc = x.find('span', class_='s-item__price').text
                    shp = x.find('span', class_='s-item__shipping s-item__logisticsCost').text
                    link = x.find('a')['href']

                    _writer.writerow([name, state, prc, shp, link])


                except:
                    pass

    return _writer


if __name__ == '__main__':
    scrap()



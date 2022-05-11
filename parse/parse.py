import requests
from bs4 import BeautifulSoup

URL = 'https://ru.tradingview.com/markets/stocks-russia/market-movers-large-cap/'
#HEADERS = {}

def get_html(url, params=None):
    r = requests.get(url, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr', class_='row-arjDAkRm listRow')
    share = []
    for item in items:
        share.append({
            'Название акции':item.find('sup', class_='apply-common-tooltip').get_text(),
            'Тикер':item.find('a', class_='apply-common-tooltip').get_text()
        })
    print(share)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Ошибка')



parse()


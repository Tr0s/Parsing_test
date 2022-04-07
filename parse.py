import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/search/?category_id=0&marka_id=0&model_id=0&city%5B0%5D=16&state%5B0%5D=16&s_yers%5B0%5D=0&po_yers%5B0%5D=0&price_ot=&price_do='
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0', 'accept': '*/*'}
HOST = 'https://auto.ria.com'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('section', class_='proposition')
    cars = []
    for item in items:
        # uah_price = 'usd_price': item.find('span', class_='green').get_text(strip=True)
        cars.append({
            'title': item.find('span', class_='item ticket-title').get_text(strip=True),
            'link': HOST + item.find('a', class_='proposition_link').get('href'),
            'usd_price': item.find('span', class_='green').get_text(strip=True)
        })
    print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()

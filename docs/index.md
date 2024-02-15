
# Homepage
## Task_1 Project

sample `code`:
```py linenums="1"
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


def product_frame():
    html_text = requests.get("https://www.nike.com/in/w/mens-basketball-shoes-3glsmznik1zy7ok").text
    soup = BeautifulSoup(html_text, 'lxml')
    men_basketball_shoe = soup.find('h1', class_="wall-header__title css-69xvwy")
    print(men_basketball_shoe.text)
    name = soup.find_all('div', class_='product-card__title')
    product_names = [i.text.strip() for i in name]
    color_ = soup.find_all('div', class_='product-card__product-count')
    avail_color = [j.text.strip() for j in color_]
    prices = soup.find_all('div', class_='product-price in__styling is--current-price css-11s12ax')
    product_prices = [k.text.strip() for k in prices]
    data = []
    for i in range(len(product_names)):
        data.append({'Product Name': product_names[i], 'Price': product_prices[i], 'Color': avail_color[i]})
    df = pd.DataFrame(data)
    print(df)


if __name__ == '__main__':
    while True:
        product_frame()
        time_wait = 10
        print(f'Waiting {time_wait}.seconds...')
        time.sleep(10)
```


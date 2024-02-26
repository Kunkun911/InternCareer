# Code info
## Codeblocks
First import all the necessary modules like `BeautifulSoup`,`requests`,`pandas` etc
```py
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
```
`bs4` package contains the BeautifulSoup function
The BeautifulSoup will produce a `soup` from the website url that contains the html source code of that website.


then I created a function name `def product_frame()` that fetches the data of "Nike Men Basketball shoes" from Nike.in website.   
 The data contains of the product's name , price, colour available.
```py
def product_frame():
    html_text =  requests.get("https://www.nike.com/in/w/mens-basketball-shoes-3glsmznik1zy7ok").text
```

With `BeautifulSoup` function we can extract the html source code and assign it a variable named `soup`.
```py
soup = BeautifulSoup(html_text, 'lxml')
```
In the `soup` we will search for data with tags and `class_`
You can find the tags and `class_` names by inspecting the website in the browser.
```py
name = soup.find_all('div', class_='product-card__title')
product_names = [i.text.strip() for i in name]
color_ = soup.find_all('div', class_='product-card__product-count')
avail_color = [j.text.strip() for j in color_]
prices = soup.find_all('div', class_='product-price in__styling is--current-price css-11s12ax')
product_prices = [k.text.strip() for k in prices]
```

Create an empty `list` and append data accordingly and make a structured dataframe with pandas.
```py
data = []
for i in range(len(product_names)):
    data.append({'Product Name': product_names[i], 'Price': product_prices[i], 'Color': avail_color[i]})
df = pd.DataFrame(data)
print(df)
```

This block of code will automate the code to execute every 10 seconds and will update the dataframe if there is any changes in the website.
```py
if __name__ == '__main__':
    while True:
        product_frame()
        time_wait = 10
        print(f'Waiting {time_wait}.seconds...')
        time.sleep(10)
```
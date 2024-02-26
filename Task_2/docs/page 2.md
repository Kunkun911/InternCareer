# Page 2
## Codeblock

import all the necessary modules in my case I only used `pandas` and `matplotlib`.
read the csv file with `.read_csv()` function.
```python
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None, 'display.max_columns', None)
df = pd.read_csv(r"C:\\Datasets\\world_population_data.csv")
```
This `World_pop()` function definition will display all the countries along with bar graph of total population in each continent.
`.filter()` is used to filter/clean the data to only display the most relevant datas.
```python
def World_pop():
    global df
    print(df.filter(items=['rank', 'country', '2023 population', '2022 population']).set_index('rank'))
    print('\n')
    ch_1 = input('Display Population graph of each continents? y/n :')
    if ch_1.lower() in ['y', 'yes']:
        asia = (df.loc[df['continent'] == 'Asia'].filter(items=['2023 population', 'country', 'rank'])
                .sort_values(by='rank', ascending=False))
        europe = (df.loc[df['continent'] == 'Europe'].filter(items=['2023 population', 'country', 'rank'])
                  .sort_values(by='rank', ascending=False))
        na = (df.loc[df['continent'] == 'North America'].filter(items=['2023 population', 'country', 'rank'])
              .sort_values(by='rank', ascending=False))
        sa = (df.loc[df['continent'] == 'South America'].filter(items=['2023 population', 'country', 'rank'])
                .sort_values(by='rank', ascending=False))
        ocean = (df.loc[df['continent'] == 'Oceania'].filter(items=['2023 population', 'country', 'rank'])
                 .sort_values(by='rank', ascending=False))
        africa = (df.loc[df['continent'] == 'Africa'].filter(items=['2023 population', 'country', 'rank'])
                    .sort_values(by='rank', ascending=False))

        # Asia Graph
        a = asia['2023 population'].tolist()
        c = asia['country'].tolist()

        plt.figure(1, figsize=(15, 12))
        barplot = plt.barh(y=c, width=a, fc="lightgray", ec="black")
        plt.bar_label(barplot, labels=a, label_type="edge", padding=5)
        plt.xlabel("2023 population")
        plt.ylabel("Countries in Asia")
        plt.title('Asia')
        plt.show()

        # Europe Graph
        a2 = europe['2023 population'].tolist()
        c2 = europe['country'].tolist()

        plt.figure(2, figsize=(15, 12))
        barplot2 = plt.barh(y=c2, width=a2, fc="lightgray", ec="black")
        plt.bar_label(barplot2, labels=a2, label_type="edge", padding=5)
        plt.xlabel("2023 population")
        plt.ylabel("Countries in Europe")
        plt.title('Europe Population Graph')
        plt.show()

        # South America Graph
        a3 = sa['2023 population'].tolist()
        c3 = sa['country'].tolist()

        plt.figure(3, figsize=(15, 12))
        barplot3 = plt.barh(y=c3, width=a3, fc="lightgray", ec="black")
        plt.bar_label(barplot3, labels=a3, label_type="edge", padding=5)
        plt.xlabel("2023 population")
        plt.ylabel("Countries in South America")
        plt.title('South America Population Graph')
        plt.show()

        # North America Graph
        a4 = na['2023 population'].tolist()
        c4 = na['country'].tolist()

        plt.figure(4, figsize=(15, 12))
        barplot4 = plt.barh(y=c4, width=a4, fc="lightgray", ec="black")
        plt.bar_label(barplot4, labels=a4, label_type="edge", padding=5)
        plt.xlabel("2023 population")
        plt.ylabel("Countries in North America")
        plt.title('North America Population Graph')
        plt.show()

        # Oceania graph
        a5 = ocean['2023 population'].tolist()
        c5 = ocean['country'].tolist()

        plt.figure(5, figsize=(15, 12))

        barplot5 = plt.barh(y=c5, width=a5, fc="lightgray", ec="black")
        plt.bar_label(barplot5, labels=a5, label_type="edge", padding=5)
        plt.xlabel("2023 population")
        plt.ylabel("Countries in Oceania")
        plt.title('Oceania Population Graph')
        plt.show()

        # Africa Graph
        a6 = africa['2023 population'].tolist()
        c6 = africa['country'].tolist()

        plt.figure(6, figsize=(15, 12))

        barplot6 = plt.barh(y=c6, width=a6, fc="lightgray", ec="black")
        plt.bar_label(barplot6, labels=a6, label_type="edge", padding=5)
        plt.xlabel("2023 population")
        plt.ylabel("Countries in Africa")
        plt.title('Africa Population Graph')
        plt.show()
    else:
        print('\n')
```
This block of code is used to find a specific country.
```python
def country():
    global df
    choose_ctry = input("Enter the country Name: ").title()
    country1 = df[df['country'].isin([choose_ctry])]

    if country1.empty:
        print("No such Country", choose_ctry, "\nEnter a valid Country Name")
        country()
    else:
        print(country1.filter(items=['rank', 'country', '2023 population', 'world percentage', 'continent']))

```
The `Compare()` will compare the population between two user given countries and produce a pie chart displaying the comparison.
```python
def Compare():
    global df
    ctry1 = input("Enter the First country Name: ").title()
    ctry2 = input("Enter the Second country Name: ").title()
    
    country1 = df.loc[df['country'] == ctry1].filter(items=['2023 population'])
    country2 = df.loc[df['country'] == ctry2].filter(items=['2023 population'])
    cname = [ctry1, ctry2]
    ctr1_pop = country1['2023 population'].tolist()
    ctr2_pop = country2['2023 population'].tolist()
    data = ctr1_pop + ctr2_pop
    try:
        plt.pie(data, labels=cname, autopct='%1.1f%%',
                startangle=90,
                wedgeprops={"edgecolor": "black",
                            'linewidth': 2,
                            'antialiased': True})
        plt.axis('equal')
        plt.show()
    except:
        print("Enter valid Country Name")
```
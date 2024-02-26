
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

df = pd.read_csv(r"C:\\Datasets\\world_population_data.csv")
'''
with open("C:\\Datasets\\world_population_data.csv",'r') as f:
    file = f.read()
    f.close()

'''
def World_pop():
    global df
    print(df.filter(items=['rank', 'country', '2023 population']))
    popu = df.filter(items=['2023 population', '2022 population', '2020 population', '2015 population', '2010 population', '2000 population'])
    asia = df.loc[df['continent'] == 'Asia']
    europe = df.loc[df['continent'] == 'Europe']
    na = df.loc[df['continent'] == 'North America']
    sa = df.loc[df['continent'] == 'South America']
    ocean = df.loc[df['continent'] == 'Oceania']
    africa = df.loc[df['continent'] == 'Africa']

    plt.figure(1)
    asia.plot(kind='bar',
            x='country',
            y='2023 population',
            color='red')

    # set the title
    plt.title('Asia')

    # show the plot
    plt.show()
    plt.figure(2)
    europe.plot(kind='bar',
              x='country',
              y='2023 population',
              color='orange')

    # set the title
    plt.title('Europe')

    # show the plot
    plt.show()
    plt.figure(3)
    sa.plot(kind='bar',
              x='country',
              y='2023 population',
              color='pink')

    # set the title
    plt.title('South America')

    # show the plot
    plt.show()
    plt.figure(4)
    na.plot(kind='bar',
              x='country',
              y='2023 population',
              color='yellow')

    # set the title
    plt.title('North America')

    # show the plot
    plt.show()
    plt.figure(5)
    ocean.plot(kind='bar',
              x='country',
              y='2023 population',
              color='green')

    # set the title
    plt.title('Oceania')

    # show the plot
    plt.show()
    plt.figure(6)
    africa.plot(kind='bar',
              x='country',
              y='2023 population',
              color='blue')

    # set the title
    plt.title('Africa')

    # show the plot
    plt.show()

World_pop()
'''
def country():
    global df
    choose_ctry = input("Enter the country Name: ").title()
    country1 = df[df['country'].isin([choose_ctry])]

    if country1.empty:
        print("No such Country", choose_ctry, "\nEnter a valid Country Name")
        country()
    else:
        print(country1.filter(items = ['rank','country','2023 population','world percentage','continent']))
country()

def Compare():
    global df
    no_ctry = int("Enter the number of countries you want to compare: ")
    ctrys = []
    for i in range(no_ctry):
        choose_ctry = input("Enter the country Name: ").title()
        ctrys.append(choose_ctry)
        print(country1.filter(items = ['rank','country','2023 population','world percentage','continent']))


def Top10():
    global df
    top_10 = df.head(10)
    print(top_10.filter(items=['rank', 'country', '2023 population', 'world percentage', 'continent']))
    top_10.plot(kind='bar',
              x='country',
              y='2023 population',
              color='red')
    plt.title('Graph')
    plt.show()


def Last10():
    global df
    last_10 = df.tail(10)
    print(last_10.filter(items = ['rank','country','2023 population','world percentage','continent']))
Last10()

while True :
    ch1 = int(input("Enter Your choice: "))
    print("1. Show world Population.")
    print("2. Choose a specific country.")
    print("3. Compare Countries.")
    print("4. Display Top 10.")
    print("5. Display Last 10.")
    print("6. Display Graphs.")
    print("7. Choose an Other CSV file.)
    print("8. Exit")
    if ch == 1:
        World_pop()
    elif ch == 2:
        country()
    elif ch == 3:
        Compare()

    elif ch == 4:
        
    elif ch == 5:

    elif ch == 6:

    elif ch == 7:

    else:
        if ch == 8:
            break
        else:
            continue
'''
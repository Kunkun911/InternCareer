
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None, 'display.max_columns', None)
df = pd.read_csv(r"C:\\Datasets\\world_population_data.csv")

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

def country():
    global df
    choose_ctry = input("Enter the country Name: ").title()
    country1 = df[df['country'].isin([choose_ctry])]

    if country1.empty:
        print("No such Country", choose_ctry, "\nEnter a valid Country Name")
        country()
    else:
        print(country1.filter(items=['rank', 'country', '2023 population', 'world percentage', 'continent']))


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

def Top10():
    global df
    top_10 = df.head(10).filter(items=['rank', 'country', '2023 population', 'world percentage', 'continent'])
    print(top_10)
    data = top_10['2023 population'].tolist()
    ctry = top_10['country'].tolist()
    ch_1 = input('Display Population graph of Top 10 Countries? y/n :')
    if ch_1.lower() in ['y', 'yes']:
        plt.figure(1, figsize=(17, 10))
        bar_plot = plt.barh(y=ctry, width=data, fc="lightgray", ec="black")
        plt.bar_label(bar_plot, labels=data, label_type="edge", padding=5)
        plt.xlabel("2023 population")
        plt.ylabel("Countries")
        plt.title('Top 10')
        plt.show()
    else:
        print('')


def Last10():
    global df
    last_10 = df.tail(10).filter(items=['rank','country', '2023 population', 'world percentage', 'continent'])
    print(last_10)
    data = last_10['2023 population'].tolist()
    ctry = last_10['country'].tolist()
    ch_1 = input('Display Population graph of Last 10 Countries? y/n :')
    if ch_1.lower() in ['y', 'yes']:
        plt.figure(1, figsize=(17, 10))
        bar_plot = plt.barh(y=ctry, width=data, fc="lightgray", ec="black")
        plt.bar_label(bar_plot, labels=data, label_type="edge", padding=5)
        plt.xlabel("2023 population")
        plt.ylabel("Countries")
        plt.title('Last 10')
        plt.show()
    else:
        print()

def stats():
    a = df.agg(
        {
         '2023 population': ['sum', 'mean', 'median', 'max', 'min', 'std'],
         "2022 population": ['sum', 'mean', 'median', 'max', 'min', 'std'],
         "2020 population": ['sum', 'mean', 'median', 'max', 'min', 'std']
         }
    )
    print(a)

def new_csv(path):
    df2 = pd.read_csv(path, encoding='unicode_escape')
    while True:
        print('1. Display the Dataframe.')
        print('2. Display the First 10.')
        print('3. Display the Last 10.')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            print(df2)
        elif choice == '2':
            print(df2.head(10))
        elif choice == '3':
            print(df2.tail(10))
        else:
            break

while True :
    print("1. Show world Population.")
    print("2. Choose a specific country.")
    print("3. Compare Countries.")
    print("4. Display Top 10.")
    print("5. Display Last 10.")
    print("6. Show Summary Statistics")
    print("7. Choose an Other CSV file.")
    print("8. Exit")
    ch = input("Enter Your choice: ")
    if ch == '1':
        World_pop()
    elif ch == '2':
        country()
    elif ch == '3':
        Compare()
    elif ch == '4':
        Top10()
    elif ch == '5':
        Last10()
    elif ch == '6':
        stats()
    elif ch == '7':
        # Enter the path without the quote/ double quote
        path1 = input('Enter the path of the file: ')
        new_csv(path1)
    else:
        if ch == '8':
            break
        else:
            print("$$\nInvalid Option\n$$\nChoose again")
            continue


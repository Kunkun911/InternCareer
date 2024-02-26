# Page 3
## CodeBlock

These two `Top10()` and `Last10()` will show the top 10 most populated and top 10 least populated countries respectively.
```python
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

```
To show the summary statistics of the dataset.
```python
def stats():
    a = df.agg(
        {
         '2023 population': ['sum', 'mean', 'median', 'max', 'min', 'std'],
         "2022 population": ['sum', 'mean', 'median', 'max', 'min', 'std'],
         "2020 population": ['sum', 'mean', 'median', 'max', 'min', 'std']
         }
    )
    print(a)
```
You can also use a different csv file to read data and display.
```python
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
```
These will keep the whole code running in loop unless the user wants to exit.
```python
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
```
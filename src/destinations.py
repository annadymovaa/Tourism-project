import pandas as pd
from random import randint
import csv

#ф-ция для 
def m_to_season(months: list) -> set:
    seasons = {'winter' : ['Dec', 'Jan', 'Feb'], 
            'spring' : ['Mar', 'Apr', 'May'],
            'summer' : ['Jun', 'Jul', 'Aug'],
            'fall' : ['Sep', 'Oct', 'Nov']}
    for i in range(len(months)):
        if months[i] in seasons['winter']:
            months[i] = 'winter'
        elif months[i] in seasons['spring']:
            months[i] = 'spring'
        elif months[i] in seasons['summer']:
            months[i] = 'summer'
        else:
            months[i] = 'fall'
    return set(months)

def generate_number(number: int) -> int:
    return round(randint(1000,100000), -2)

def category(df: pd.DataFrame) -> set:
    # category = df['Category'].str.replace(r"\s*\([^)]*\)", '', regex=True)
    # print(category)
    # category = category.str.split(', ')
    category = df['Category']
    cats = set()
    for i in range(category.count()):
        for j in category[i]:
            cats.add(j)
    return cats



if __name__ == "__main__":
    file_path = 'data/travel_destinations.csv'

    df = pd.read_csv(file_path)

    cat = df['Category'].str.replace(r"\s*\([^)]*\)", '', regex=True)
    df['Category'] = cat.str.split(', ')

    #category сейчас записывается в csv preferences.csv
    categories = category(df)
    cats = pd.DataFrame(categories)
    cats.to_csv('data/preferences.csv')
    # df.drop(columns=['Category'], inplace=True)
    #пока не стоит удалять столбец 'Category', чтобы потом была возможность реализовать связь многие-ко-многим
    
    df['Best_season'] = df['Best_Time_to_Travel'].str.split(', ').apply(m_to_season)
    df.drop(columns=['Best_Time_to_Travel'], inplace=True)
    df['Average_price'] = 0
    df['Average_price'] = df['Average_price'].apply(generate_number)
    print(df.head(5))
    # df.to_csv("data/destinations.csv")
    
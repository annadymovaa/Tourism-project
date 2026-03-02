import pandas as pd
from random import randint

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


if __name__ == "__main__":
    file_path = 'data/travel_destinations.csv'

    df = pd.read_csv(file_path)

    print(df.head()) 

    #category обработать

    df['Best_season'] = df['Best_Time_to_Travel'].str.split(', ').apply(m_to_season)

    df['Average_price'] = 0
    df['Average_price'] = df['Average_price'].apply(generate_number)
    
    print(df.head())
from faker import Faker
from random import randint
import csv

def generate(i):
    fake = Faker('ru_RU')
    user = {
        'user_id' : i + 1,
        'first_name' : fake.first_name(),
        'last_name' : fake.last_name(),
        'gender' : fake.random_element(elements = ('м', 'ж')),
        'birthday' : fake.date_of_birth(minimum_age=15, maximum_age = 80),
        'country' : fake.random_element(elements = ('Россия', 'Беларусь')),
        'preferred_tour_type' : fake.random_element(elements = ('Пляжный', 'Семейный', 'Активный', 'Экскурсионный')),
        'budget'  : round(randint(10000, 1000000), -4)
    }
    return user

def users_data():
    users = list()

    for i in range(2000):
        user = generate(i)
        users.append(user)
    return users

users = users_data()

with open('users.csv', 'w', newline='', encoding='utf-8') as file:
    writer  = csv.DictWriter(file, fieldnames = users[0].keys())
    writer.writeheader()
    writer.writerows(users)


from random import random, randint
from faker import Faker
import csv


NROWS = 100
fake = Faker("ru_RU")

def generate_user(fake: Faker):
    fullname = fake.name()
    birthday = fake.date_of_birth(minimum_age=14, maximum_age=90)
    country_of_birth = fake.country()
    country = fake.current_country()
    region = fake.region()
    city_name = fake.city_name()
    address = fake.street_address()
    client_id = randint(10 ** 9, 10 ** 10 - 1)
    inn = fake.individuals_inn()
    phone = fake.phone_number()
    email = fake.email()
    return fullname, birthday, country_of_birth, country, region,city_name, address, client_id, inn, phone, email

def generate_users_rows(fake: Faker, NROWS: int):
    clients = []
    for i in range(NROWS):
        row = generate_user(fake)
        clients.append(row)
    return clients

if __name__ == "__main__":
    with open( "/Users/ekaterinaprokopeva/Desktop/Aston_Project/fraud_detection/data/clients.csv", "w", encoding="utf-8", newline=""
    ) as file:
        writer = csv.writer(file, delimiter=";")
        for i in range(NROWS):
            row = generate_user(fake)
            writer.writerow(row)


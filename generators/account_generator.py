import random
from faker import Faker
import csv
from datetime import datetime, timedelta

MAX_ACC_NUM = 10
fake = Faker("ru_RU")


def generate_account(client_id: int, fake: Faker):
    accounts = []
    accounts_number_per_client = random.randint(0, MAX_ACC_NUM)
    for _ in range(accounts_number_per_client):
        account_id = random.randint(10**10, 10**11 - 1)
        account_type = random.choice(["Текущий", "Сберегательный", "Кредитный"])
        bic = fake.bic()
        korr_account = fake.correspondent_account()
        open_date = fake.date_time_between(datetime.now() - timedelta(days=365), datetime.now())
        status = random.choice(['Closed', 'Active', 'Frozen'])
        account_number = f"{client_id}{account_id}" # уникальный номер счета
        accounts.append([client_id, int(account_number), account_type, bic, korr_account, open_date, status ])
    return accounts
               

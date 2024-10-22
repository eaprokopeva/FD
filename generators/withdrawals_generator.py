from datetime import datetime, timedelta
import random
from faker import Faker
import csv

fake = Faker("ru_RU")
MAX_NUM_WITHDRAWALS = 10

# Функция для генерации операций снятия наличных, включая возможность аномальных
def generate_cash_withdrawals(account_id: int, fake: Faker):
    withdrawals = []

    for _ in range(random.randint(1, MAX_NUM_WITHDRAWALS)):
        # Генерация данных снятия наличных
        transaction_id = fake.uuid4()
        transaction_date = fake.date_time_between(datetime.now() - timedelta(days=365), datetime.now())
        amount = round(random.uniform(1000, 50000))
        atm_location = fake.city_name()

        if random.random() < 0.05:  
            amount = round(random.uniform(100001, 500000))

        # Добавление данных о снятии наличных в список
        withdrawals.append([account_id,transaction_id, transaction_date, amount, atm_location])

    return withdrawals

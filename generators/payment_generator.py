from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker("ru_RU")
MAX_NUM_TRANSACTIONS = 50

# Функция для генерации транзакций, включая возможность аномальных
def generate_transactions(card_id: int, fake: Faker):
    transactions = []
    
    for _ in range(random.randint(1, MAX_NUM_TRANSACTIONS)):

        # Генерация даты и времени транзакции
        transaction_id = fake.uuid4()
        transaction_date = fake.date_time_between(datetime.now() - timedelta(days=365), datetime.now())
        merchant_name = fake.company()
        amount = round(random.uniform(10, 1000), 2)
        category = random.choice(["groceries", "electronics", "clothing", "restaurants", "travel", 
              "entertainment", "utilities", "health", "fuel", "online_services"])
        location = fake.city_name()

        if random.random() < 0.05:
            fraud_type = random.choice(["large_amount", "night_time"])
            if fraud_type == "large_amount":
                amount = round(random.uniform(10000, 50000), 2)
            else:
                # Покупка в ночное время (с 00:00 до 06:00) на сумму более 5000
                transaction_date = fake.date_time_between_dates(datetime_start=transaction_date.replace(hour=0), 
                                                                datetime_end=transaction_date.replace(hour=6))
                amount = round(random.uniform(5001, 10000), 2)

        transactions.append([card_id, transaction_id, transaction_date, merchant_name, amount, category, location])

    return transactions

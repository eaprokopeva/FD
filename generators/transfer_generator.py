from datetime import datetime, timedelta
import random
from faker import Faker

fake = Faker("ru_RU")
MAX_NUM_TRANSFERS = 10

def generate_transfers(account_id: int, fake: Faker):
    transfers = []

    for _ in range(random.randint(1, MAX_NUM_TRANSFERS)):
        # Генерация данных перевода
        transaction_id = fake.uuid4()
        transaction_date = fake.date_time_between(datetime.now() - timedelta(days=365), datetime.now())
        destination_account_id = random.randint(10**10, 10**11 - 1)
        amount = round(random.uniform(1000, 50000), 2)

        if random.random() < 0.05:  
            fraud_type = random.choice(["large_amount", "repeated_large_transfer"])
            if fraud_type == "large_amount":
                # Перевод на сумму более 100000
                amount = round(random.uniform(100001, 500000), 2)
            else:
                # Две транзакции на сумму от 25000 до 50000 с разницей во времени 1 час
                amount = round(random.uniform(25000, 50000), 2)
                
                # Вторая транзакция в течение часа после первой
                second_transaction_id = fake.uuid4()
                second_transaction_date = fake.date_time_between_dates(datetime_start=transaction_date, 
                                                                datetime_end=transaction_date + timedelta(hours = 1))
                second_amount = round(random.uniform(25000, 50000), 2)
                transfers.append([account_id, second_transaction_id, destination_account_id, second_transaction_date, second_amount])

        # Добавление данных о переводе в список
        transfers.append([account_id, transaction_id, destination_account_id, transaction_date, amount])

    return transfers

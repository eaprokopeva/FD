import random
from faker import Faker
import csv
from datetime import datetime, timedelta

MAX_CARD_NUM = 5
fake = Faker("ru_RU")


def generate_card(account_number: int, start_date: datetime, fake: Faker):
    cards = []
    cards_number_per_account = random.randint(0, MAX_CARD_NUM)
    for _ in range(cards_number_per_account):
        card_id = fake.credit_card_number()
        card_provider = fake.credit_card_provider()
        expire_date = fake.credit_card_expire(start = start_date)
        status = random.choice(['Active', 'Frozen'])
        cards.append([account_number, card_id, card_provider, expire_date, status ])
    return cards
               

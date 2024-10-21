import csv
from faker import Faker
from clients_generator import generate_users_rows
from account_generator import generate_account
from card_generator import generate_card

NROWS = 100  # Количество клиентов
fake = Faker("ru_RU")

def write_to_csv(filename: str, data: list):
    """Записывает данные в CSV файл."""
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)  # Запись данных

if __name__ == "__main__":
    # Генерация клиентов
    clients = generate_users_rows(fake, NROWS)
    write_to_csv("clients.csv", clients)

    # Генерация счетов
    all_accounts = []
    for client in clients:
        client_id = client[7]  # Client ID находится в 8-м элементе списка
        accounts = generate_account(client_id, fake)
        all_accounts.extend(accounts)  # Собираем все счета в один список

    write_to_csv("accounts.csv", all_accounts)

    # Генерация карт для текущих и кредитных счетов
    all_cards = []
    for account in all_accounts:
        account_number = account[1]  # Номер счета находится во 2-м элементе списка
        account_type = account[2]  # Тип счета находится в 3-м элементе списка
        if account_type in ["Текущий", "Кредитный"]:  # Проверяем, является ли счет текущим или кредитным
            cards = generate_card(account_number, account[5], fake)
            all_cards.extend(cards)  # Собираем все карты в один список

    write_to_csv("cards.csv", all_cards)

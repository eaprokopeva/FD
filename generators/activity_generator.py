import random
from datetime import datetime, timedelta
from faker import Faker


# Инициализация Faker
fake = Faker("ru_RU")
MAX_NUM_SESSIONS = 25

# Функция для генерации активности клиентов
def generate_user_activity(client_id: int, fake: Faker):
    activities = []
    base_location = fake.city_name()
    
    for _ in range(0, random.randint(0, MAX_NUM_SESSIONS)):
        session_id = fake.uuid4()

        if random.random() < 0.1:
            location = fake.city_name() 
        else:
            location = base_location 

        device_type = random.choice(["desktop", "mobile", "tablet"])
        ip_address = fake.ipv4()
        browser_info = fake.user_agent()

        num_actions = random.randint(1, 5)
        for _ in range(num_actions):
            action_time = fake.date_time_between(datetime.now() - timedelta(days=365), datetime.now())
            action_type = random.choice(["login", "logout", "update_profile", "recover_password"])
            activities.append([client_id, action_time, action_type, device_type, ip_address, location, session_id, browser_info])
    return activities

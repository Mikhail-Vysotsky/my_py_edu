import json
from faker import Faker

fake_ru = Faker('ru_RU')

def print_formated_json(user_list):
    jsn = json.dumps(user_list, indent=4, ensure_ascii=False,)
    #parsed = json.loads(jsn)
    print(jsn)

def generate_test_users(count=10): # где 10 - кол-во сгенерированных пользователей
    """Генерация тестовых пользователей для системы"""
    users = []
    for i in range(count):
        user = {
            "id": i + 1, # Уникальный идентификатор, начинается с 1
            "personal_info": {
                "name": fake_ru.name(), # Случайное ФИО на русском
                "birth_date": fake_ru.date_of_birth().isoformat(), # Дата рождения в формате ISO
                "gender": fake_ru.random_element(["M", "F"]), # Пол (М/Ж) 
                "documents": {
                    "passport": fake_ru.passport_number(), # Номер паспорта
                    "snils": fake_ru.snils() # Номер СНИЛС
                }
            },
            "contact_info": {
                "email": fake_ru.email(), # Электронная почта
                "phone": fake_ru.phone_number(), # Номер телефона
                "address": fake_ru.address() # Адрес
            },
            "work_info": {
                "company": fake_ru.company(), # Название компании
                "position": fake_ru.job(), # Должность
                "salary": fake_ru.random_int(30000, 200000) # Зарплата от 30к до 200к
            },
            "system_info": {
                "registration_date": fake_ru.date_this_year().isoformat(), # Дата регистрации
                "last_login": fake_ru.date_time_this_month().isoformat(), # Последний вход
                "is_active": fake_ru.boolean(chance_of_getting_true=80) # 80% активных пользователей
            }
        }
        users.append(user)
    return users


print_formated_json(generate_test_users(10))


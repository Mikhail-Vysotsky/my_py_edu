import json
from faker import Faker

def print_formated_json(user_list):
    jsn = json.dumps(user_list, indent=4, ensure_ascii=False,)
    #parsed = json.loads(jsn)
    print(jsn)

fake = Faker('ru_RU')
users = [{
    "name": fake.name(),
    "email": fake.email(),
    "phone": fake.phone_number(),
    "gender": fake.random_element(["M", "F"]),
    "bank": fake.bank(),
    "credit_card": fake.credit_card_number(), 
    "card_expired": fake.credit_card_expire(),
    "cvv": fake.credit_card_security_code(),
    "card_provider": fake.credit_card_provider()
} for _ in range(5)]

print_formated_json(users)


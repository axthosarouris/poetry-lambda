from faker import Faker


def handle_request(event, context) -> str:
    random_string = Faker.pystr(10)
    return random_string

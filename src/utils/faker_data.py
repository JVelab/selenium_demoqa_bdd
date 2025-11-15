from faker import Faker

faker = Faker()

def generate_user_data():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "mobile": faker.random_number(digits=10)
    }

from faker import Faker

faker = Faker()

print("Generating dummy data...")
def generate_dummy_data(num_records=10):
    dummy_data = []
    for _ in range(num_records):
        record = {
            "name": faker.name(),
            "address": faker.address(),
            "email": faker.email(),
            "phone_number": faker.phone_number(),
            "company": faker.company(),
            "job": faker.job(),
        }
        dummy_data.append(record)
    return dummy_data

print(generate_dummy_data(5))
print("Dummy data generated successfully!")

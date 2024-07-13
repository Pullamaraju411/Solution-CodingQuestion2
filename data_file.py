import csv
import faker

def random_csv(file_name, num_of_records):
    fake = faker.Faker()
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_of_records):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address().replace('\n', ' '),
                'date_of_birth': fake.date_of_birth()
            })

random_csv('random_data.csv', 10**6)


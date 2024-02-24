import random
import string
from faker import Faker
import csv
import datetime
print('client started')
fake = Faker()
Array = []

def generate_id():
    global Array
    generated_id = fake.random_number(digits=6)
    Array.append(generated_id)
    return generated_id

def generate_first_name():
    return fake.first_name()

def generate_last_name():
    return fake.last_name()

def generate_address():
    return fake.address()

def generate_date_of_birth():
    return fake.date_of_birth(minimum_age=18, maximum_age=90)

def generate_email():
    return fake.email()

def generate_phone_number():
    return fake.phone_number()

def generate_agence():
    return fake.company()

def generate_membership_date():
    return fake.date_between(start_date='-5y', end_date='today')

def generate_gender():
    genders = ["Male", "Female"]
    return random.choice(genders)

def generate_age(date_of_birth):
    today = datetime.date.today()
    age = today.year - date_of_birth.year
    # Vérification pour ajuster l'âge si la date d'anniversaire n'est pas encore passée cette année
    if today.month < date_of_birth.month or (today.month == date_of_birth.month and today.day < date_of_birth.day):
        age -= 1
    return age

def generate_random_data(num_entries):
    data = []
    for _ in range(num_entries):
        date_of_birth = generate_date_of_birth()
        entry = {
            "Id_client": generate_id(),
            "First Name": generate_first_name(),
            "Last Name": generate_last_name(),
            "Address": generate_address(),
            "Birth Date": date_of_birth,
            "Age": generate_age(date_of_birth),  # Ajout de la case "Age"
            "Email": generate_email(),
            "Phone Number": generate_phone_number(),
            "Agency": generate_agence(),
            "Membership Date": generate_membership_date(),
            "Gender": generate_gender()
        }

        data.append(entry)

    return data

# Exemple d'utilisation
random_data = generate_random_data(7000)
print("client generated")
# Define CSV file path
csv_file = "../datasets/Client.csv"

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = random_data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(random_data)

print("Data has been written to the CSV file:", csv_file)

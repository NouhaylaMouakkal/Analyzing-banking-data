import random
import string
import csv
from collections import defaultdict
from Dataset_Client import Array
print('account start')
def generate_rib():
    rib = ''.join(random.choices(string.digits, k=10))
    return rib

def generate_amount():
    amount = round(random.uniform(0, 10000), 2)
    amount_with_currency = f"{amount} dhs"
    return amount_with_currency

def generate_expiration_date():
    year = random.randint(2023, 2030)
    month = random.randint(1, 12)
    expiration_date = f"{month}/{year}"
    return expiration_date

def generate_verification_code():
    code = ''.join(random.choices(string.digits, k=3))
    return code

def generate_card_type():
    card_types = ["Visa", "Mastercard", "American Express"]
    card_type = random.choice(card_types)
    return card_type

def generate_account_type():
    account_types = ["Courant", "Epargne", "CourantEpargne"]
    account_type = random.choice(account_types)
    return account_type

def generate_client_id():
    idClient = Array[:]  # Copie les ID de la variable Array
    array = []
    repetitions = {}

    # Compte le nombre de répétitions de chaque ID existant
    for id in idClient:
        if id in repetitions:
            repetitions[id] += 1
        else:
            repetitions[id] = 1

    # Génère un tableau avec un nombre de répétitions variant de 1 à 3
    for id, count in repetitions.items():
        repetitions_left = min(3 - count, 3)  # Limite le nombre de répétitions restantes à 3
        array.extend([id] * repetitions_left)

    # Choisi un ID de client aléatoire dans le tableau
    idClient = random.choice(array)
    array.remove(idClient)  # Supprime l'ID choisi pour éviter de le répéter plus de 3 fois

    return idClient

def generate_random_data(num_entries):
    data = []
    account_types_set = set()  # Set to store unique account types for each client

    for _ in range(num_entries):
        rib = generate_rib()
        amount = generate_amount()
        expiration_date = generate_expiration_date()
        verification_code = generate_verification_code()
        card_type = generate_card_type()

        id_client = generate_client_id()
        account_type = generate_account_type()

        entry = {
            "RIB": rib,
            "Amount": amount,
            "Expiration_date": expiration_date,
            "Verification_code": verification_code,
            "Card_type": card_type,
            "Account_type": account_type,
            "Id_client": id_client  # Add the foreign key for client ID
        }

        data.append(entry)

    return data

def count_accounts_per_user(csv_file_cpt):
    # Create a defaultdict to store the count of accounts per user
    accounts_per_user = defaultdict(int)

    # Read the CSV file
    with open(csv_file_cpt, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id_client = row["Id_client"]
            accounts_per_user[id_client] += 1

    return accounts_per_user

# Generate random data
random_data = generate_random_data(10000)
print('account generated')
# Define CSV file path
csv_file_cpt = "../datasets/Compte.csv"

# Write data to CSV file
with open(csv_file_cpt, mode='w', newline='') as file:
    fieldnames = random_data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(random_data)

print("Data has been written to the CSV file:", csv_file_cpt)
accounts_count = count_accounts_per_user(csv_file_cpt)
print("\nAccounts per user:", accounts_count)
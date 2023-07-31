import random
import string

companies_data = []


def generate_random_cnpj():
    return ''.join(random.choices(string.digits, k=14))


def generate_random_name(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))


fixed_cnae = ['6202-3', '6209-1', '6204-0']


for _ in range(50):
    new_company = {
        'CNPJ': generate_random_cnpj(),
        'nome_razao': generate_random_name(),
        'nome_fantasia': generate_random_name(),
        'CNAE': fixed_cnae
    }
    companies_data.append(new_company)

# Print the new companies_data with 50 additional registries
print(companies_data)

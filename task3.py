def is_valid_client_format(client):
    if (not isinstance(client, tuple) or len(client) != 3 or
        not all(isinstance(item, str) for item in client)):
        return False

    name, status, email = client
    if name == "" or status == "" or email == "":
        return False

    return True

def count_client_statuses(clients_data, status_count):
    status = clients_data[1]
    if status:
        status_count[status] = status_count.get(status, 0) + 1

def collect_invalid_emails(clients_data, invalid_emails):
    email = clients_data[2]
    if "@" not in email or not isinstance(email, str):
        invalid_emails.append(email)

def identify_new_clients(clients_data, new_clients):
    name, status, email = clients_data
    if status == "новий" and name and "@" in email:
        new_clients.append(name)

def analyze_clients(clients):
    status_count = {}
    invalid_emails = []
    new_clients = []
    errors = []

    for client in clients:
        if not is_valid_client_format(client):
            errors.append(client)
            continue

        count_client_statuses(client, status_count)
        collect_invalid_emails(client, invalid_emails)
        identify_new_clients(client, new_clients)

    return {
        "status_count": status_count,
        "invalid_emails": invalid_emails,
        "new_clients": new_clients,
        "errors": errors
    }

result = analyze_clients([
    ("Іван", "новий", "ivan@email.com"),
    ("Олена", "постійний", "olena[at]mail.com"),
    ("", "новий", "ivan@email.com"), # некоректне ім'я
    ("Олена", "", "olena[at]mail.com"), # некоректний статус
    ("Іван", "новий", ""), # некоректний email
    ("", "", ""), # два некоректних поля (ім'я і статус)
    ("Петро", "", ""), # два некоректних поля (статус і email)
    "не кортеж", # невірний формат даних
    123, # невірний формат даних
    None, # невірний формат даних
    ("Олена",), # невірний формат всередині кортежу
    ("Іван", "новий"), # невірний формат всередині кортежу
    (123, "новий", "ivan@email.com"), # невірний тип для імені
    ("Іван", 123, "ivan@email.com"), # невірний тип для статусу
    ("Іван", "новий", 123), # невірний тип для email
])

import pprint
pprint.pprint(result)
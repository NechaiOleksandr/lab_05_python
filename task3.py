def analyze_clients(clients):
    status_count = {}
    invalid_emails = []
    new_clients = []
    errors = []

    for client in clients:
        if (not isinstance(client, tuple) or len(client) != 3 or
            not all(isinstance(item, str) for item in client)):
            errors.append(client)
            continue

        name, status, email = client

        if name == "" or status == "" or email == "":
            errors.append(client)

        if status:
            status_count[status] = status_count.get(status, 0) + 1

        if "@" not in email:
            invalid_emails.append(email)

        if status == "новий" and name and "@" in email:
            new_clients.append(name)

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
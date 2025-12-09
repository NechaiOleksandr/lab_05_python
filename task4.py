from datetime import datetime


def is_valid_date(date_str, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except (ValueError, TypeError):
        return False


def analyze_expenses(expenses):
    result = {
        "category_totals": {},
        "max_expense": None,
        "invalid_dates": [],
        "errors": []
    }

    for item in expenses:
        if not isinstance(item, tuple) or len(item) != 3:
            result["errors"].append(item)
            continue

        amount, category, date_str = item

        is_amount_valid = isinstance(amount, (int, float))
        is_category_valid = isinstance(category, str)
        is_date_type_valid = isinstance(date_str, str)

        if not (is_amount_valid and is_category_valid and is_date_type_valid):
            result["errors"].append(item)
            continue

        if not is_valid_date(date_str):
            result["invalid_dates"].append(date_str)
            continue

        if category in result["category_totals"]:
            result["category_totals"][category] += amount
        else:
            result["category_totals"][category] = amount

        if result["max_expense"] is None:
            result["max_expense"] = item
        else:
            if amount > result["max_expense"][0]:
                result["max_expense"] = item

    return result

result = analyze_expenses([
    (100, "офіс", "2024-06-01"),
    (200, "маркетинг", "2024-06-02"),
    (50, "офіс", "2024-13-01"),  # некоректний запис дати
    (None, "маркетинг", "2024-06-02"),  # некоректна сума
    (100, None, "2024-06-01"),  # некоректна категорія
    (100, "офіс", None),  # некоректна дата (тип)
    "не кортеж",  # невірний формат даних
    123,  # невірний формат даних
    None,  # невірний формат даних
    (100, "офіс"),  # невірний формат всередині кортежу
    (100,),  # невірний формат всередині кортежу
    (100, "офіс", "2024-06-01", "extra")  # зайвий елемент
])

import pprint
pprint.pprint(result)
from datetime import datetime


def is_valid_date(date_str, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except (ValueError, TypeError):
        return False


def validate_expense_item(item):
    if not isinstance(item, tuple) or len(item) != 3:
        return False

    amount, category, date_str = item

    is_amount_valid = isinstance(amount, (int, float))
    is_category_valid = isinstance(category, str)
    is_date_type_valid = isinstance(date_str, str)

    return is_amount_valid and is_category_valid and is_date_type_valid


def update_category_totals(category_totals, amount, category):
    category_totals[category] = category_totals.get(category, 0) + amount


def track_max_expense(current_max, item):
    amount = item[0]

    if current_max is None:
        return item

    max_amount = current_max[0]

    if amount > max_amount:
        return item

    return current_max


def analyze_expenses(expenses):
    result = {
        "category_totals": {},
        "max_expense": None,
        "invalid_dates": [],
        "errors": []
    }

    for item in expenses:
        if not validate_expense_item(item):
            result["errors"].append(item)
            continue

        amount, category, date_str = item

        if not is_valid_date(date_str):
            result["invalid_dates"].append(date_str)
            continue

        update_category_totals(result["category_totals"], amount, category)

        result["max_expense"] = track_max_expense(result["max_expense"], item)

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
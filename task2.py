def flatten_dictionaries(data):
    dictionaries = []
    if isinstance(data, dict):
        dictionaries.append(data)
    elif isinstance(data, list):
        for item in data:
            dictionaries.extend(flatten_dictionaries(item))
    return dictionaries


def find_categories(dictionaries):
    categories = set()
    for dictionary in dictionaries:
        categories.update(dictionary.keys())
    return categories


def calculate_sums(dictionaries, categories):
    sums = {category: 0 for category in categories}
    for dictionary in dictionaries:
        for category, value in dictionary.items():
            if category in sums:
                sums[category] += value
    return sums


def analyze_nested_categories(data):
    dictionaries = flatten_dictionaries(data)
    categories = find_categories(dictionaries)
    sums = calculate_sums(dictionaries, categories)
    return categories, sums

nested_data = [
[
{"офіс": 100},
{"маркетинг": 200}
],
[
[
{"офіс": 50},
{"маркетинг": 150}
],
{"офіс": 200}
],
{"офіс": 300},
[{"офіс": 100, "extra": 1}]
]
result = analyze_nested_categories(nested_data)
print(result)
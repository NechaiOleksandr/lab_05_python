def filter_reports(reports, output_format, keyword):
    filtered_reports = []
    errors = []

    for report in reports:
        if not isinstance(report, tuple):
            errors.append(report)
            continue

        if len(report) != 3:
            errors.append(report)
            continue

        title, author, format = report

        if not (isinstance(title, str) and isinstance(author, str) and isinstance(format, str)):
            errors.append(report)
            continue

        if not title or not author or not format:
            errors.append(report)
            continue

        if format == output_format:
            if keyword in title or keyword in author:
                filtered_reports.append(report)

    return {
        "filtered_reports": filtered_reports,
        "count": len(filtered_reports),
        "errors": errors
    }


# --- Тестування (Зразок виклику) ---
result = filter_reports(
    [
        ("Звіт1", "Іван Іванов", "pdf"),
        ("Звіт2", "Олена Петрівна", "docx"),
        ("", "Іван Іванов", "pdf"),  # некоректна назва
        ("Звіт3", "", "pdf"),  # некоректний автор
        ("Звіт4", "Петро Сидоров", ""),  # некоректний формат
        "не кортеж",  # невірний формат даних
        123,  # невірний формат даних
        None,  # невірний формат даних
        ("Звіт5",),  # невірний формат всередині кортежу
        ("Звіт6", "Іван Іванов"),  # невірний формат всередині кортежу
        ("Звіт7", "Іван Іванов", 123),  # невірний тип для формату
    ],
    "pdf",
    "Іва"
)

import pprint
pprint.pprint(result)
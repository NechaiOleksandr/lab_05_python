def validate_report(report):
    if not isinstance(report, tuple) or len(report) != 3:
        return False

    if not all(isinstance(item, str) for item in report):
        return False

    title, author, format_type = report

    if not title or not author or not format_type:
        return False

    return True


def criteria(report, output_format, keyword):
    title, author, format_type = report
    format_match = format_type == output_format
    keyword_match = keyword in title or keyword in author
    return format_match and keyword_match


def filter_reports(reports, output_format, keyword):
    valid_reports = []
    errors = []

    for report in reports:
        if validate_report(report):
            valid_reports.append(report)
        else:
            errors.append(report)

    filtered_reports = []

    for report in valid_reports:
        if criteria(report, output_format, keyword):
            filtered_reports.append(report)

    return {
        "filtered_reports": filtered_reports,
        "count": len(filtered_reports),
        "errors": errors
    }

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
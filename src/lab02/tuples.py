def format_record(rec: tuple[str, str, float]) -> str:
    """
    Форматирует запись студента в строку.

    Аргументы:
    rec -- кортеж (fio: str, group: str, gpa: float)

    Возвращает:
    str -- форматированная строка вида "Фамилия И.И., гр. Группа, GPA X.XX"

    Исключения:
    ValueError -- если ФИО или группа пусты
    TypeError -- если GPA не является числом
    """
    fio, group, gpa = rec

    if not fio.strip():
        raise ValueError("ФИО не может быть пустым")
    if not group.strip():
        raise ValueError("Группа не может быть пустой")
    if not isinstance(gpa, (float, int)):
        raise TypeError("GPA должен быть числом")

    # Убираем лишние пробелы и разбиваем ФИО на части
    parts = fio.strip().split()
    parts = [part.strip() for part in parts if part.strip()]

    # Формируем инициалы
    if len(parts) >= 3:
        initials = f"{parts[0].capitalize()} {parts[1][0].upper()}.{parts[2][0].upper()}."
    elif len(parts) == 2:
        initials = f"{parts[0].capitalize()} {parts[1][0].upper()}."
    else:
        initials = parts[0].capitalize()  # На случай, если ФИО некорректно

    # Форматируем GPA с 2 знаками после запятой
    gpa_formatted = f"{gpa:.2f}"

    return f"{initials}, гр. {group}, GPA {gpa_formatted}"


# Задание 5 — Инициалы и длина строки
#
# Файл: src/05_initials_and_len.py
# Ввод: ФИО одной строкой (могут быть лишние пробелы).
# Вывод: инициалы (верхний регистр) и длина исходной строки без лишних пробелов.
#
# Пример:
#
# ФИО:   Иванов   Иван   Иванович
# Инициалы: ИИИ.
# Длина (символов): 20

full_name = input("ФИО: ").strip()
parts = full_name.split()
full_name_no_spaces = ''.join(part.strip() for part in parts)
full_name_no_spaces_len = len(full_name_no_spaces)
initials = ''.join(part[0].upper() for part in parts)
length = len(full_name)
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {full_name_no_spaces_len + 2}") # +2 for the spaces between initials
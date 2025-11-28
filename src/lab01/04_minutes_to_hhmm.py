# Задание 4 — Минуты → ЧЧ:ММ
#
# Файл: src/04_minutes_to_hhmm.py
# Ввод: m — целые минуты.
# Вывод: ЧЧ:ММ минуты вывести как {min:02d}.
#
# Пример:
#
# Минуты: 135
# 2:15

m = int(input("Минуты: "))
hours = m // 60
minutes = m % 60
print(f"{hours}:{minutes:02d}")
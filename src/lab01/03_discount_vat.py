# Задание 3 — Чек: скидка и НДС
#
# Файл: src/03_discount_vat.py
# Ввод: price (₽), discount (%), vat (%) — вещественные.
# Формулы:
# base = price * (1 - discount/100)
# vat_amount = base * (vat/100)
# total = base + vat_amount
# Вывод: по строкам, 2 знака после запятой.
#
# База после скидки: 900.00 ₽
# НДС:               180.00 ₽
# Итого к оплате:    1080.00 ₽
#
# (пример входных: price=1000, discount=10, vat=20)

price = float(input("Цена (₽): ").replace(',', '.'))
discount = float(input("Скидка (%): ").replace(',', '.'))
vat = float(input("НДС (%): ").replace(',', '.'))
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")

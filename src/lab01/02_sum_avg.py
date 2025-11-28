# Ввод: два числа (вещественные), допускаются точка или запятая.
# Вывод: sum=<...>; avg=<...> — значения печатать с 2 знаками.
#
# Пример:
#
# a: 3,5
# b: 4.25
# sum=7.75; avg=3.88

a = input("a: ").replace(',', '.')
b = input("b: ").replace(',', '.')
a = float(a)
b = float(b)
_sum = a + b
_avg = _sum / 2
print(f"sum={_sum:.2f}; avg={_avg:.2f}")
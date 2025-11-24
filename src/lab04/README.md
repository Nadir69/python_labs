ok
~/projects/python_labs$ python src/lab04/text_report.py --in data/samples/text_example.txt --out data/out/report.csv
Всего слов: 166
Уникальных слов: 126
Топ-5:
там:14
и:9
на:5
я:4
без:2

data/input.txt не существует → понятная ошибка в консоли
~/projects/python_labs$ python src/lab04/text_report.py
Error: Input file 'data/input.txt' not found.


Пустой вход → report.csv будет содержать только заголовок или будет пустым (примите решение и опишите — рекомендую только заголовок).
~/projects/python_labs$ python src/lab04/text_report.py --in data/samples/empty.txt --out data/out/report.cs
v
Всего слов: 0
Уникальных слов: 0
Топ-5:

~/projects/python_labs$ cat data/out/report.csv
word,count

~/projects/python_labs$ python src/lab04/text_report.py --in data/samples/text_example_cp1251.txt --out data/out/report.csv --encoding cp1251
Всего слов: 168
Уникальных слов: 10
Топ-5:
пїѕпїѕпїѕ:32
пїѕпїѕпїѕпїѕпїѕ:26
пїѕпїѕпїѕпїѕпїѕпїѕ:25
пїѕ:23
пїѕпїѕпїѕпїѕ:21
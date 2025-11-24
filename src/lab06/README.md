# python src/lab06/cli_text.py cat --input data/samples/people.csv
# $ python src/lab06/cli_text.py cat --input data/samples/people.csv -n
# 1       name,age,city
# 2       Alice,22,SPB
# 3       Bob,25,Moscow
# 4       Carlos,30,Kazan
# 5       Dana,21,SPB
# 6       Andrey,27,Novosibirsk
# $ python src/lab06/cli_text.py cat --input data/samples/people.csv
# name,age,city
# Alice,22,SPB
# Bob,25,Moscow
# Carlos,30,Kazan
# Dana,21,SPB
# Andrey,27,Novosibirsk


$ python src/lab06/cli_text.py stats --input data/samples/text_example.txt 
freqencies: {'у': 2, 'лукоморья': 1, 'дуб': 2, 'зеленый': 2, 'златая': 1, 'цепь': 1, 'на': 5, 'дубе': 1, 'том': 1, 'и': 9, 'днем': 1, 'ночью': 1, 'кот
': 2, 'ученый': 2, 'все': 1, 'ходит': 1, 'по': 1, 'цепи': 1, 'кругом': 1, 'идет': 2, 'направо': 1, 'песнь': 1, 'заводит': 1, 'налево': 1, 'сказку': 2,
 'говорит': 1, 'там': 14, 'чудеса': 1, 'леший': 1, 'бродит': 1, 'русалка': 1, 'ветвях': 1, 'сидит': 1, 'неведомых': 1, 'дорожках': 1, 'следы': 1, 'нев
иданных': 1, 'зверей': 1, 'избушка': 1, 'курьих': 1, 'ножках': 1, 'стоит': 1, 'без': 2, 'окон': 1, 'дверей': 1, 'лес': 1, 'дол': 1, 'видений': 1, 'пол
ны': 1, 'о': 1, 'заре': 1, 'прихлынут': 1, 'волны': 1, 'брег': 1, 'песчаный': 1, 'пустой': 1, 'тридцать': 1, 'витязей': 1, 'прекрасных': 1, 'чредой': 
1, 'из': 1, 'вод': 1, 'выходят': 1, 'ясных': 1, 'с': 2, 'ними': 1, 'дядька': 1, 'их': 1, 'морской': 1, 'королевич': 1, 'мимоходом': 1, 'пленяет': 1, '
грозного': 1, 'царя': 1, 'в': 2, 'облаках': 1, 'перед': 1, 'народом': 1, 'через': 2, 'леса': 1, 'моря': 2, 'колдун': 1, 'несет': 1, 'богатыря': 1, 'те
мнице': 1, 'царевна': 1, 'тужит': 1, 'а': 1, 'бурый': 1, 'волк': 1, 'ей': 1, 'верно': 1, 'служит': 1, 'ступа': 1, 'бабою': 1, 'ягой': 1, 'бредет': 1, 
'сама': 1, 'собой': 1, 'царь': 1, 'кащей': 1, 'над': 1, 'златом': 1, 'чахнет': 1, 'русской': 1, 'дух': 1, 'русью': 1, 'пахнет': 1, 'я': 4, 'был': 1, '
мед': 1, 'пил': 1, 'видел': 1, 'под': 1, 'ним': 1, 'сидел': 1, 'свои': 1, 'мне': 1, 'сказки': 1, 'говорил': 1, 'одну': 1, 'помню': 1, 'эту': 1, 'поведаю': 1, 'теперь': 1, 'свету': 1}


$ python src/lab06/cli_text.py stats --input data/samples/text_example.txt --top 6
там:14
и:9
на:5
я:4
без:2
в:2


[//]: # (cli_convert.py)
[//]: # ($ activate python env)
[//]: # (cd python_labs)
[//]: # ($ export PYTHONPATH=.)

$ python src/lab06/cli_convert.py json2csv --help
usage: cli_convert.py json2csv [-h] --in INPUT --out OUTPUT

Конвертация JSON в CSV

options:
  -h, --help    show this help message and exit
  --in INPUT    Входной JSON файл
  --out OUTPUT  Выходной CSV файл


$ python src/lab06/cli_convert.py csv2json --help
usage: cli_convert.py csv2json [-h] --in INPUT --out OUTPUT

Конвертация CSV в JSON

options:
  -h, --help    show this help message and exit
  --in INPUT    Входной CSV файл
  --out OUTPUT  Выходной JSON файл

$ python src/lab06/cli_convert.py csv2xlsx --help
usage: cli_convert.py csv2xlsx [-h] --in INPUT --out OUTPUT

Конвертация CSV в XLSX

options:
  -h, --help    show this help message and exit
  --in INPUT    Входной CSV файл
  --out OUTPUT  Выходной XLSX файл

python src/lab06/cli_convert.py json2csv --in data/samples/people.json --out data/out/people_from_cli.csv
->
Создан data/out/people_from_cli.csv

python src/lab06/cli_convert.py csv2json --in data/samples/people.csv --out data/out/people_from_cli
.json
->
Создан data/out/people_from_cli.json

python src/lab06/cli_convert.py csv2xlsx --in data/samples/people.csv --out data/out/people_from_cli.xlsx
->
Создан data/out/people_from_cli.xlsx
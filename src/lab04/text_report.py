# Напишите скрипт, который:
#
#     Читает один входной файл data/input.txt (путь можно захардкодить или принять параметром командной строки — опишите в README).
#     Нормализует текст (lib/text.py), токенизирует и считает частоты слов.
#     Сохраняет data/report.csv c колонками: word,count, отсортированными: count ↓, слово ↑ (при равенстве).
#     В консоль печатает краткое резюме:
#         Всего слов: <N>
#         Уникальных слов: <K>
#         Топ-5: (список из top_n из ЛР3)
#
# Пример запуска
#
# python src/lab04/text_report.py                 # читает data/input.txt, пишет data/report.csv
# python src/lab04/text_report.py --in data/in.txt --out data/out.csv
#
# Пример report.csv
#
# word,count
# привет,2
# мир,1
#
# Краевые случаи
#
#     data/input.txt не существует → понятная ошибка в консоли (исключение пусть всплывает или выведите print() и sys.exit(1) — опишите поведение в README).
#     Пустой вход → report.csv будет содержать только заголовок или будет пустым (примите решение и опишите — рекомендую только заголовок).
#     Нестандартная кодировка → укажите, как передать --encoding cp1251 (если реализуете argparse).

import sys
from pathlib import Path
import argparse
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def main():
    parser = argparse.ArgumentParser(description="Generate word frequency report from text file.")
    parser.add_argument("--in", dest="input_path", type=str, default="data/input.txt", help="Path to input text file")
    parser.add_argument("--out", dest="output_path", type=str, default="data/report.csv", help="Path to output CSV file")
    parser.add_argument("--encoding", dest="encoding", type=str, default="utf-8", help="File encoding (default: utf-8)")
    args = parser.parse_args()

    input_path = Path(args.input_path)
    output_path = Path(args.output_path)
    encoding = args.encoding

    try:
        # Read input file
        input_text = read_text(input_path, encoding=encoding)

        # Normalize and tokenize text
        normalized_text = normalize(input_text)
        tokens = tokenize(normalized_text)

        # Count word frequencies
        freq = count_freq(tokens)

        # Prepare data for CSV
        rows = [(word, count) for word, count in freq.items()]
        rows.sort(key=lambda x: (-x[1], x[0]))  # Sort by count desc, word asc

        # Write to CSV
        write_csv(rows, output_path, header=("word", "count"))

        # Print summary
        total_words = len(tokens)
        unique_words = len(freq)
        top_5 = top_n(freq, n=5)

        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_5:
            print(f"{word}:{count}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Cannot decode file '{input_path}' with encoding '{encoding}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()

# Пример запуска
# python src/lab04/text_report.py                 # читает data/input.txt, пишет data/report.csv
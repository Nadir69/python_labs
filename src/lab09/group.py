import csv
from pathlib import Path
from typing import List
from src.lab08.models import Student
class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str) -> None:
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        if not self.path.is_file():
            with self.path.open(mode="w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self) -> List[Student]:
        students = []
        with self.path.open(mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    student = Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"]),
                    )
                    students.append(student)
                except (ValueError, KeyError):
                    continue
        return students

    def list(self) -> List[Student]:
        return self._read_all()

    def add(self, student: Student) -> None:
        with self.path.open(mode="a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([student.fio, student.birthdate, student.group, student.gpa])

    def find(self, substr: str) -> List[Student]:
        students = self._read_all()
        return [s for s in students if substr.lower() in s.fio.lower()]

    def remove(self, fio: str) -> None:
        students = self._read_all()
        students = [s for s in students if s.fio != fio]
        with self.path.open(mode="w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.HEADER)
            for student in students:
                writer.writerow([student.fio, student.birthdate, student.group, student.gpa])

    def update(self, fio: str, **fields) -> None:
        students = self._read_all()
        for student in students:
            if student.fio == fio:
                for key, value in fields.items():
                    if hasattr(student, key):
                        setattr(student, key, value)
                        # self.remove(fio)
        with self.path.open(mode="w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.HEADER)
            for student in students:
                writer.writerow([student.fio, student.birthdate, student.group, student.gpa])

    def stats(self) -> dict:
        students = self._read_all()
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": [],
            }

        count = len(students)
        gpas = [student.gpa for student in students]
        min_gpa = min(gpas)
        max_gpa = max(gpas)
        avg_gpa = sum(gpas) / count

        groups = {}
        for student in students:
            groups[student.group] = groups.get(student.group, 0) + 1

        top_5_students = sorted(students, key=lambda s: s.gpa, reverse=True)[:5]
        top_5_students = [{"fio": student.fio, "gpa": student.gpa} for student in top_5_students]

        return {
            "count": count,
            "min_gpa": min_gpa,
            "max_gpa": max_gpa,
            "avg_gpa": avg_gpa,
            "groups": groups,
            "top_5_students": top_5_students,
        }
# Пример использования:
# if __name__ == "__main__":
#     current_directory = Path(__file__).parent.parent
#     root_directory = current_directory.parent
#     group = Group(f"{root_directory}\\data\\lab09\\students.csv")
#
#     # Добавление студентов
#     student1 = Student(fio="Иванов Иван Иванович", birthdate="2000-01-15", group="SE-01", gpa=4.5)
#     student2 = Student(fio="Петров Петр Петрович", birthdate="1999-05-20", group="SE-02", gpa=3.8)
#     group.add(student1)
#     group.add(student2)
#
#     # Вывод всех студентов
#     all_students = group.list()
#     for student in all_students:
#         print(student)
#
#     # Поиск студентов по подстроке в fio
#     found_students = group.find("Иванов")
#     for student in found_students:
#         print("Найден:", student)
#
#     # Обновление студента
#     group.update("Иванов Иван Иванович", gpa=5.0)
#
#     # Удаление студента
#     group.remove("Петров Петр Петрович")
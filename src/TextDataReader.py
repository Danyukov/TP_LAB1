# -*- coding: utf-8 -*-
from DataReader import DataReader
from Types import DataType


class TextDataReader(DataReader):
    def read(self, path: str) -> DataType:
        students: DataType = {}
        current_student: str | None = None

        with open(path, encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.strip()

                if not line:
                    continue

                # Если это строка со студентом:
                #  - заканчивается на ":"  ИЛИ
                #  - не содержит ":" вообще
                if line.endswith(":") and line.count(":") == 1:
                    current_student = line[:-1].strip()
                    students.setdefault(current_student, [])
                    continue

                if ":" not in line:
                    # считаем, что это тоже имя студента
                    current_student = line.strip()
                    students.setdefault(current_student, [])
                    continue

                # Иначе это "предмет:балл"
                if current_student is None:
                    raise ValueError("Invalid TXT format: subject without student")

                subject, score_str = line.split(":", 1)
                subject = subject.strip()
                score_str = score_str.strip()

                if subject == "":
                    raise ValueError("Invalid TXT format: empty subject")

                try:
                    score = int(score_str)
                except ValueError as exc:
                    raise ValueError(
                        f"Invalid TXT format: score must be int, got '{score_str}'"
                    ) from exc

                students[current_student].append((subject, score))

        return students

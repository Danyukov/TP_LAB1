# -*- coding: utf-8 -*-
from DataReader import DataReader
from Types import DataType
import yaml


class YAMLDataReader(DataReader):
    """
    Поддерживает 2 структуры YAML:
    1) Список:
       - "Имя Фамилия":
           предмет: балл
    2) Словарь в корне:
       "Имя Фамилия":
         предмет: балл
    """

    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as f:
            loaded = yaml.safe_load(f)

        if loaded is None:
            return {}

        students_map: dict[str, dict[str, int]] = {}

        if isinstance(loaded, dict):
            for student_name, subj_map in loaded.items():
                if not isinstance(subj_map, dict):
                    raise ValueError(
                        "Invalid YAML: student's value must be a map"
                    )
                students_map[str(student_name)] = {
                    str(k): int(v) for k, v in subj_map.items()
                }

        elif isinstance(loaded, list):
            for item in loaded:
                if not isinstance(item, dict) or len(item) != 1:
                    raise ValueError(
                        "Invalid YAML: each list item must be a single-key map"
                    )
                student_name = next(iter(item.keys()))
                subj_map = item[student_name]
                if not isinstance(subj_map, dict):
                    raise ValueError(
                        "Invalid YAML: student's value must be a map"
                    )
                students_map[str(student_name)] = {
                    str(k): int(v) for k, v in subj_map.items()
                }
        else:
            raise ValueError(
                "Invalid YAML root type. Expected list or dict."
            )

        result: DataType = {}
        for student_name, subj_map in students_map.items():
            result[student_name] = [
                (subj, int(score)) for subj, score in subj_map.items()
            ]
        return result

# -*- coding: utf-8 -*-
from Types import DataType


class ExcellentStudentsCounter:
    def __init__(self, data: DataType, threshold: int = 90) -> None:
        self.data: DataType = data
        self.threshold: int = threshold

    def count(self) -> int:
        excellent_count = 0
        for student, subjects in self.data.items():
            if len(subjects) == 0:
                continue
            if all(score >= self.threshold for _, score in subjects):
                excellent_count += 1
        return excellent_count

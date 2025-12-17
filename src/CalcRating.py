# -*- coding: utf-8 -*-
from Types import DataType


class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: dict[str, float] = {}

    def calc(self) -> dict[str, float]:
        self.rating = {}

        for student, subjects in self.data.items():
            if len(subjects) == 0:
                self.rating[student] = 0.0
                continue

            total = 0
            for _, score in subjects:
                total += score

            self.rating[student] = total / len(subjects)

        return self.rating

# -*- coding: utf-8 -*-
from ExcellentStudentsCounter import ExcellentStudentsCounter
from Types import DataType


class TestExcellentStudentsCounter:
    def test_count_excellent(self) -> None:
        data: DataType = {
            "A": [("math", 90), ("prog", 91)],
            "B": [("math", 100), ("prog", 100), ("lit", 90)],
            "C": [("math", 89), ("prog", 95)],
            "D": [("math", 90), ("prog", 88)],
            "E": [],
        }
        assert ExcellentStudentsCounter(data).count() == 2

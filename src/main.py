# -*- coding: utf-8 -*-
import argparse
import os
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from YAMLDataReader import YAMLDataReader
from ExcellentStudentsCounter import ExcellentStudentsCounter


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p",
        dest="path",
        type=str,
        required=True,
        help="Path to datafile",
    )
    parsed = parser.parse_args(args)
    return parsed.path


def get_reader_by_path(path: str):
    ext = os.path.splitext(path)[1].lower()
    if ext in [".yaml", ".yml"]:
        return YAMLDataReader()
    return TextDataReader()


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = get_reader_by_path(path)
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    excellent_count = ExcellentStudentsCounter(students).count()
    print("Excellent students count (all scores >= 90): ", excellent_count)


if __name__ == "__main__":
    main()

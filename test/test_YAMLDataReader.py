# -*- coding: utf-8 -*-
import pytest
from Types import DataType
from YAMLDataReader import YAMLDataReaderr


class TestYAMLDataReader:
    @pytest.fixture()
    def yaml_list_text_and_data(self) -> tuple[str, DataType]:
        text = (
            "- Иванов Константин Дмитриевич:\n"
            "    математика: 91\n"
            "    химия: 100\n"
            "- Петров Петр Семенович:\n"
            "    русский язык: 87\n"
            "    литература: 78\n"
        )
        data: DataType = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91),
                ("химия", 100),
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87),
                ("литература", 78),
            ],
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data_list(
        self, yaml_list_text_and_data, tmpdir
    ) -> tuple[str, DataType]:
        p = tmpdir.mkdir("yamldir").join("students.yaml")
        p.write_text(yaml_list_text_and_data[0], encoding="utf-8")
        return str(p), yaml_list_text_and_data[1]

    def test_read_list_root(
        self, filepath_and_data_list: tuple[str, DataType]
    ) -> None:
        file_content = YAMLDataReader().read(filepath_and_data_list[0])
        assert file_content == filepath_and_data_list[1]

    def test_read_dict_root(self, tmpdir) -> None:
        text = (
            "Иванов Иван Иванович:\n"
            "  математика: 90\n"
            "  физика: 95\n"
            "Петров Петр Петрович:\n"
            "  химия: 61\n"
        )
        expected: DataType = {
            "Иванов Иван Иванович": [("математика", 90), ("физика", 95)],
            "Петров Петр Петрович": [("химия", 61)],
        }

        p = tmpdir.mkdir("yamldir2").join("students.yml")
        p.write_text(text, encoding="utf-8")

        file_content = YAMLDataReader().read(str(p))
        assert file_content == expected

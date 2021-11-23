import unittest

from data import load


file_names = [
    "output_test/Membros ativos-contracheque-02-2020.ods",
    "output_test/Membros ativos-Verbas Indenizatorias-02-2020.ods",
]


class TestData(unittest.TestCase):
    # Validação para ver se a planilha não foi apagada no processo...
    def test_validate_existence(self):
        STATUS_DATA_UNAVAILABLE = 4
        with self.assertRaises(SystemExit) as cm:
            dados = load(file_names, "2021", "01")
            dados.validate()
        self.assertEqual(cm.exception.code, STATUS_DATA_UNAVAILABLE)


if __name__ == "__main__":
    unittest.main()
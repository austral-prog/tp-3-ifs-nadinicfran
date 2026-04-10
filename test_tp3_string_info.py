import io
import unittest.mock
import string_info as ex1


class TP3StringInfoTestCases(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_string_info(self, mock_stdout):
        ex1.string_info()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "Palabra: Programacion")
        self.assertEqual(results[1], "Longitud: 12")
        self.assertEqual(results[2], "Primera letra: P")
        self.assertEqual(results[3], "Ultima letra: n")
        self.assertEqual(results[4], "Repetida: ProgramacionProgramacionProgramacion")
        self.assertEqual(results[5], "Decorada: ***Programacion***")


if __name__ == '__main__':
    unittest.main()

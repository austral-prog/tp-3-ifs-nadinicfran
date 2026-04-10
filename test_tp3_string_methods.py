import io
import unittest.mock
import string_methods as ex1


class TP3StringMethodsTestCases(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_string_methods(self, mock_stdout):
        ex1.string_methods()
        results = mock_stdout.getvalue().splitlines()

        # strip, lstrip, rstrip
        self.assertEqual(results[0], "Strip: Grace Hopper")
        self.assertEqual(results[1], "Lstrip: Grace Hopper   ")
        self.assertEqual(results[2], "Rstrip:    Grace Hopper")

        # upper, lower, title
        self.assertEqual(results[3], "Upper: PYTHON ES UN GRAN LENGUAJE DE PROGRAMACION")
        self.assertEqual(results[4], "Lower: python es un gran lenguaje de programacion")
        self.assertEqual(results[5], "Title: Python Es Un Gran Lenguaje De Programacion")

        # find
        self.assertEqual(results[6], "Find: 13")

        # replace
        self.assertEqual(results[7], "Replace: Python es un gran lenguaje de desarrollo")

        # count
        self.assertEqual(results[8], "Count: 4")

        # in
        self.assertEqual(results[9], "Contiene Python: True")
        self.assertEqual(results[10], "Contiene Java: False")

        # slicing
        self.assertEqual(results[11], "Slice: Python")

        # slicing con paso (no contiguo)
        self.assertEqual(results[12], "Paso: Pto")

        # slicing reverso
        self.assertEqual(results[13], "Reverso: nohtyP")

        # f-string
        self.assertEqual(results[14], "Formato: Grace Hopper sabe Python")

        # multilinea
        self.assertEqual(results[15], "Linea 1")
        self.assertEqual(results[16], "Linea 2")
        self.assertEqual(results[17], "Linea 3")


if __name__ == '__main__':
    unittest.main()

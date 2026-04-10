import io
import unittest.mock
import ficha as ex1


class TP3FichaTestCases(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ficha_maria(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=[
            "   maria GARCIA   ", "Maria.Garcia@Universidad.EDU", "8", "9", "7"
        ]):
            ex1.ficha()
            results = mock_stdout.getvalue().splitlines()

            # Multiline string + string repetition
            self.assertEqual(results[0], "========================")
            self.assertEqual(results[1], "    FICHA DEL ALUMNO")
            self.assertEqual(results[2], "========================")

            # strip + title
            self.assertEqual(results[3], "Nombre: Maria Garcia")

            # lower
            self.assertEqual(results[4], "Email: maria.garcia@universidad.edu")

            # len
            self.assertEqual(results[5], "Caracteres en nombre: 12")

            # find + indexing
            self.assertEqual(results[6], "Iniciales: MG")

            # find + slicing + lower + concatenation
            self.assertEqual(results[7], "Usuario: garcia.maria")

            # in operator
            self.assertEqual(results[8], "Email valido: True")

            # find + slicing
            self.assertEqual(results[9], "Dominio: universidad.edu")

            # replace
            self.assertEqual(results[10], "Nombre para archivo: Maria_Garcia")

            # count
            self.assertEqual(results[11], "Cantidad de a: 4")

            # reverse slicing + upper
            self.assertEqual(results[12], "Codigo secreto: AICRAG AIRAM")

            # int casting
            self.assertEqual(results[13], "Nota 1: 8")
            self.assertEqual(results[14], "Nota 2: 9")
            self.assertEqual(results[15], "Nota 3: 7")

            # math: +, /, //
            self.assertEqual(results[16], "Suma: 24")
            self.assertEqual(results[17], "Promedio: 8.0")
            self.assertEqual(results[18], "Promedio entero: 8")

            # string repetition
            self.assertEqual(results[19], "========================")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_ficha_juan(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=[
            "   JUAN perez   ", "Juan.Perez@Escuela.COM", "6", "9", "6"
        ]):
            ex1.ficha()
            results = mock_stdout.getvalue().splitlines()

            self.assertEqual(results[0], "========================")
            self.assertEqual(results[1], "    FICHA DEL ALUMNO")
            self.assertEqual(results[2], "========================")
            self.assertEqual(results[3], "Nombre: Juan Perez")
            self.assertEqual(results[4], "Email: juan.perez@escuela.com")
            self.assertEqual(results[5], "Caracteres en nombre: 10")
            self.assertEqual(results[6], "Iniciales: JP")
            self.assertEqual(results[7], "Usuario: perez.juan")
            self.assertEqual(results[8], "Email valido: True")
            self.assertEqual(results[9], "Dominio: escuela.com")
            self.assertEqual(results[10], "Nombre para archivo: Juan_Perez")
            self.assertEqual(results[11], "Cantidad de a: 1")
            self.assertEqual(results[12], "Codigo secreto: ZEREP NAUJ")
            self.assertEqual(results[13], "Nota 1: 6")
            self.assertEqual(results[14], "Nota 2: 9")
            self.assertEqual(results[15], "Nota 3: 6")
            self.assertEqual(results[16], "Suma: 21")
            self.assertEqual(results[17], "Promedio: 7.0")
            self.assertEqual(results[18], "Promedio entero: 7")
            self.assertEqual(results[19], "========================")


if __name__ == '__main__':
    unittest.main()

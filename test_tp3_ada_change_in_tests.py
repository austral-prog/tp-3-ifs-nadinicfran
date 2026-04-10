import io
import unittest.mock
import names as ex1
import change as ex3


class TP2TestCases(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_names_ada(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=["AdA", "LoVeLAce"]):
            ex1.names()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "ada lovelace")
            self.assertEqual(results[1], "Ada Lovelace")
            self.assertEqual(results[2], "ADA LOVELACE")
            self.assertEqual(results[3], "\tada lovelace")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_names_alan(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=["aLaN", "tURiNg"]):
            ex1.names()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "alan turing")
            self.assertEqual(results[1], "Alan Turing")
            self.assertEqual(results[2], "ALAN TURING")
            self.assertEqual(results[3], "\talan turing")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_change(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=["23.75", "100"]):
            ex3.change()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Ingresar gasto:")
            self.assertEqual(results[1], "23.75")
            self.assertEqual(results[2], "Dinero recibido")
            self.assertEqual(results[3], "100")
            self.assertEqual(results[4], "")
            self.assertEqual(results[5], "Vuelto")
            self.assertEqual(results[6], "")
            self.assertEqual(results[7], "Pesos:")
            self.assertEqual(results[8], "76")
            self.assertEqual(results[9], "Centavos:")
            self.assertEqual(results[10], "25")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_change_2(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=["67.40", "200"]):
            ex3.change()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Ingresar gasto:")
            self.assertEqual(results[1], "67.4")
            self.assertEqual(results[2], "Dinero recibido")
            self.assertEqual(results[3], "200")
            self.assertEqual(results[4], "")
            self.assertEqual(results[5], "Vuelto")
            self.assertEqual(results[6], "")
            self.assertEqual(results[7], "Pesos:")
            self.assertEqual(results[8], "132")
            self.assertEqual(results[9], "Centavos:")
            self.assertEqual(results[10], "60")


if __name__ == '__main__':
    unittest.main()

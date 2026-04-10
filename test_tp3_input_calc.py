import io
import unittest.mock
import input_calc as ex1


class TP3InputCalcTestCases(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_8_5(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=["8", "5"]):
            ex1.rectangle()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Base: 8")
            self.assertEqual(results[1], "Altura: 5")
            self.assertEqual(results[2], "Area: 40")
            self.assertEqual(results[3], "Perimetro: 26")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_12_3(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=["12", "3"]):
            ex1.rectangle()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Base: 12")
            self.assertEqual(results[1], "Altura: 3")
            self.assertEqual(results[2], "Area: 36")
            self.assertEqual(results[3], "Perimetro: 30")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_6_6(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=["6", "6"]):
            ex1.rectangle()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Base: 6")
            self.assertEqual(results[1], "Altura: 6")
            self.assertEqual(results[2], "Area: 36")
            self.assertEqual(results[3], "Perimetro: 24")


if __name__ == '__main__':
    unittest.main()

import io
import unittest.mock
import casting as ex1


class TP3CastingTestCases(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_casting(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=["150", "23.5", "3"]):
            ex1.casting()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Precio: 150")
            self.assertEqual(results[1], "Descuento: 23.5")
            self.assertEqual(results[2], "Precio con descuento: 126.5")
            self.assertEqual(results[3], "Total: 379.5")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_casting_2(self, mock_stdout):
        with unittest.mock.patch('builtins.input', side_effect=["200", "50.0", "2"]):
            ex1.casting()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "Precio: 200")
            self.assertEqual(results[1], "Descuento: 50.0")
            self.assertEqual(results[2], "Precio con descuento: 150.0")
            self.assertEqual(results[3], "Total: 300.0")


if __name__ == '__main__':
    unittest.main()

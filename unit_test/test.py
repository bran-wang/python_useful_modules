import unittest
from cal import Calculator

class ModuleTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator(8, 4)

    def tearDown(self):
        pass

    def test_add(self):
        result = self.calc.add()
        self.assertEqual(result, 12)

    def test_sub(self):
        result = self.calc.sub()
        self.assertEqual(result, 4)

    def test_mul(self):
        result = self.calc.mul()
        self.assertEqual(result, 32)

    def test_div(self):
        result = self.calc.div()
        self.assertEqual(result, 2)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_sub"))
    suite.addTest(ModuleTest("test_mul"))
    suite.addTest(ModuleTest("test_div"))

    runner = unittest.TextTestRunner()
    runner.run(suite)


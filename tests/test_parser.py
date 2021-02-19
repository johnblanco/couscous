import unittest
from xls_parser import parse_xls
import os
from mockito import when


class TestParser(unittest.TestCase):

    def setUp(self):
        root_path = os.getcwd().replace('/tests', '')
        when(os).getcwd().thenReturn(root_path)

    def test_balance(self):
        res = parse_xls('Estado_De_Cuenta_xxx.xls')

        self.assertGreater(res.initial_balance, 0)
        self.assertGreater(res.end_balance, 0)

    def test_expenses(self):
        res = parse_xls('Estado_De_Cuenta_xxx.xls')

        expenses_count = len(res.expenses)

        self.assertEqual(20, expenses_count)

from django.test import TestCase


import unittest

import ddt

import task4_eiler


@ddt.ddt
class TestFoundFraction(unittest.TestCase):

    @ddt.data(
        (1000000, "Для d <= 1000000, 428570 - является числителем дроби,"
                  " которая расположена непосредственно слева от 3/7."),
        (-1, "Для d <= -1, 1 - является числителем дроби,"
             " которая расположена непосредственно слева от 3/7."),
        (-100000, "Для d <= -100000, 1 - является числителем дроби,"
                  " которая расположена непосредственно слева от 3/7."),
    )
    @ddt.unpack
    def test_found_fraction(self, delitel, exp_result):
        result = task4_eiler.found_fraction(delitel)
        self.assertEqual(result, exp_result)

    @ddt.data(
        (0, ZeroDivisionError),
        ('d', TypeError),
        ([4], TypeError),
        ((9,), TypeError),
        (None, TypeError),
    )
    @ddt.unpack
    def test_found_fraction_error(self, delitel, exp_error):
        with self.assertRaises(exp_error):
            task4_eiler.search_fraction_members(delitel)


if __name__ == '__main__':
    unittest.main()


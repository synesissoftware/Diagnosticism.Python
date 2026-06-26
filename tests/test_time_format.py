#! /usr/bin/env python3

# ######################################################################## #
# File:     tests/test_time_format.py
#
# Purpose:  Unit-tests for `diagnosticism.nanoseconds_to_string()`.
#
# Created:  24th August 2025
# Updated:  27th June 2026
#
# Copyright (c) Matthew Wilson, Synesis Information Systems Pty Ltd
# All rights reserved
#
# ######################################################################## #


import unittest

from diagnosticism import nanoseconds_to_string


class nanoseconds_to_string_tester(unittest.TestCase):
    def test_zero(self):

        self.assertEqual("0s", nanoseconds_to_string(0))
        self.assertEqual("0s", nanoseconds_to_string(0, '+'))

    def test_one_second(self):

        self.assertEqual("1s", nanoseconds_to_string(1000000000))  # 1,000,000,000

    def test_123_milliseconds(self):

        self.assertEqual("123ms", nanoseconds_to_string(123000000))  # 123,000,000

    def test_123_456_789_nanoseconds(self):

        self.assertEqual("123.4ms", nanoseconds_to_string(123456789))  # 123,456,789

    def test_strings(self):

        self.assertEqual("9ns", nanoseconds_to_string(9))
        self.assertEqual("89ns", nanoseconds_to_string(89))
        self.assertEqual("789ns", nanoseconds_to_string(789))

        self.assertEqual("6.789µs", nanoseconds_to_string(6789))  # 6,789
        self.assertEqual("56.78µs", nanoseconds_to_string(56789))  # 56,789
        self.assertEqual("456.7µs", nanoseconds_to_string(456789))  # 456,789

        self.assertEqual("3.456ms", nanoseconds_to_string(3456789))  # 3,456,789
        self.assertEqual("23.45ms", nanoseconds_to_string(23456789))  # 23,456,789
        self.assertEqual("123.4ms", nanoseconds_to_string(123456789))  # 123,456,789

        self.assertEqual("9.123s", nanoseconds_to_string(9123456789))  # 9,123,456,789
        self.assertEqual("89.12s", nanoseconds_to_string(89123456789))  # 89,123,456,789
        self.assertEqual("789.1s", nanoseconds_to_string(789123456789))  # 789,123,456,789

        self.assertEqual("9ns", nanoseconds_to_string(9))
        self.assertEqual("80ns", nanoseconds_to_string(80))
        self.assertEqual("700ns", nanoseconds_to_string(700))

        self.assertEqual("6µs", nanoseconds_to_string(6000))  # 6,000
        self.assertEqual("50µs", nanoseconds_to_string(50000))  # 50,000
        self.assertEqual("400µs", nanoseconds_to_string(400000))  # 400,000

        self.assertEqual("3ms", nanoseconds_to_string(3000000))  # 3,000,000
        self.assertEqual("20ms", nanoseconds_to_string(20000000))  # 20,000,000
        self.assertEqual("100ms", nanoseconds_to_string(100000000))  # 100,000,000

        self.assertEqual("9s", nanoseconds_to_string(9000000000))  # 9,000,000,000
        self.assertEqual("10s", nanoseconds_to_string(10000000000))  # 10,000,000,000
        self.assertEqual("200s", nanoseconds_to_string(200000000000))  # 200,000,000,000
        self.assertEqual("3000s", nanoseconds_to_string(3000000000000))  # 3,000,000,000,000
        self.assertEqual("40000s", nanoseconds_to_string(40000000000000))  # 40,000,000,000,000
        self.assertEqual("500000s", nanoseconds_to_string(500000000000000))  # 500,000,000,000,000
        self.assertEqual("6000000s", nanoseconds_to_string(6000000000000000))  # 6,000,000,000,000,000
        self.assertEqual("70000000s", nanoseconds_to_string(70000000000000000))  # 70,000,000,000,000,000

        self.assertEqual("11.11s", nanoseconds_to_string(11111111111))  # 11,111,111,111
        self.assertEqual("222.2s", nanoseconds_to_string(222222222222))  # 222,222,222,222
        self.assertEqual("3333s", nanoseconds_to_string(3333333333333))  # 3,333,333,333,333
        self.assertEqual("44444s", nanoseconds_to_string(44444444444444))  # 44,444,444,444,444
        self.assertEqual("555555s", nanoseconds_to_string(555555555555555))  # 555,555,555,555,555
        self.assertEqual("6666666s", nanoseconds_to_string(6666666666666666))  # 6,666,666,666,666,666
        self.assertEqual("77777777s", nanoseconds_to_string(77777777777777777))  # 77,777,777,777,777,777

    def test_negative_values_strings(self):

        self.assertEqual("-9ns", nanoseconds_to_string(-9))
        self.assertEqual("-89ns", nanoseconds_to_string(-89))
        self.assertEqual("-789ns", nanoseconds_to_string(-789))

        self.assertEqual("-6.789µs", nanoseconds_to_string(-6789))  # -6,789
        self.assertEqual("-56.78µs", nanoseconds_to_string(-56789))  # -56,789
        self.assertEqual("-456.7µs", nanoseconds_to_string(-456789))  # -456,789

        self.assertEqual("-3.456ms", nanoseconds_to_string(-3456789))  # -3,456,789
        self.assertEqual("-23.45ms", nanoseconds_to_string(-23456789))  # -23,456,789
        self.assertEqual("-123.4ms", nanoseconds_to_string(-123456789))  # -123,456,789

        self.assertEqual("-9.123s", nanoseconds_to_string(-9123456789))  # -9,123,456,789

        self.assertEqual("-9ns", nanoseconds_to_string(-9))
        self.assertEqual("-80ns", nanoseconds_to_string(-80))
        self.assertEqual("-700ns", nanoseconds_to_string(-700))

        self.assertEqual("-6µs", nanoseconds_to_string(-6000))  # -6,000
        self.assertEqual("-50µs", nanoseconds_to_string(-50000))  # -50,000
        self.assertEqual("-400µs", nanoseconds_to_string(-400000))  # -400,000

        self.assertEqual("-3ms", nanoseconds_to_string(-3000000))  # -3,000,000
        self.assertEqual("-20ms", nanoseconds_to_string(-20000000))  # -20,000,000
        self.assertEqual("-100ms", nanoseconds_to_string(-100000000))  # -100,000,000

        self.assertEqual("-9s", nanoseconds_to_string(-9000000000))  # -9,000,000,000
        self.assertEqual("-10s", nanoseconds_to_string(-10000000000))  # -10,000,000,000
        self.assertEqual("-200s", nanoseconds_to_string(-200000000000))  # -200,000,000,000
        self.assertEqual("-3000s", nanoseconds_to_string(-3000000000000))  # -3,000,000,000,000
        self.assertEqual("-40000s", nanoseconds_to_string(-40000000000000))  # -40,000,000,000,000

    def test_observed_edge_cases(self):

        self.assertEqual("999.7ms", nanoseconds_to_string(999772000))  # 999,772,000
        self.assertEqual("999.8ms", nanoseconds_to_string(999800000))  # 999,800,000
        self.assertEqual("999.9ms", nanoseconds_to_string(999974000))  # 999,974,000

        self.assertEqual("-999.7ms", nanoseconds_to_string(-999772000))  # -999,772,000
        self.assertEqual("-999.8ms", nanoseconds_to_string(-999800000))  # -999,800,000
        self.assertEqual("-999.9ms", nanoseconds_to_string(-999974000))  # -999,974,000

    def test_with_plus_sign(self):

        self.assertEqual("999.7ms", nanoseconds_to_string(999772000))  # 999,772,000
        self.assertEqual("999.8ms", nanoseconds_to_string(999800000))  # 999,800,000
        self.assertEqual("999.9ms", nanoseconds_to_string(999974000))  # 999,974,000

        self.assertEqual("-999.7ms", nanoseconds_to_string(-999772000))  # -999,772,000
        self.assertEqual("-999.8ms", nanoseconds_to_string(-999800000))  # -999,800,000
        self.assertEqual("-999.9ms", nanoseconds_to_string(-999974000))  # -999,974,000

        self.assertEqual("999.7ms", nanoseconds_to_string(999772000, ""))  # 999,772,000
        self.assertEqual("999.8ms", nanoseconds_to_string(999800000, ""))  # 999,800,000
        self.assertEqual("999.9ms", nanoseconds_to_string(999974000, ""))  # 999,974,000

        self.assertEqual("+999.7ms", nanoseconds_to_string(999772000, '+'))  # 999,772,000
        self.assertEqual("+999.8ms", nanoseconds_to_string(999800000, '+'))  # 999,800,000
        self.assertEqual("+999.9ms", nanoseconds_to_string(999974000, '+'))  # 999,974,000


# ############################## end of file ############################# #

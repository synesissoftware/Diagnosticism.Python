#! /usr/bin/env python3

import unittest

import diagnosticism


class Package_tester(unittest.TestCase):
    def test_all_names_are_defined(self):

        for name in diagnosticism.__all__:
            self.assertTrue(hasattr(diagnosticism, name), name)

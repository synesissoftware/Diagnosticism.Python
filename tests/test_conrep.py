#!/usr/bin/env pyton

from diagnosticism.conrep import conrep as conrep

import unittest
from unittest.mock import patch

import diagnosticism

try:

    from StringIO import StringIO
except ImportError:

    from io import StringIO


class ConRep_tester(unittest.TestCase):

    def test_with_program_name(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            diagnosticism.set_program_name('myprog1')

            conrep('string-1', show_program_name=True)

            self.assertEqual('myprog1: string-1\n', fake_stderr.getvalue())

    def test_without_program_name(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            conrep('string-1', show_program_name=False)

            self.assertEqual('string-1\n', fake_stderr.getvalue())



if '__main__' == __name__:

    unittest.main()



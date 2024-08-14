#! /usr/bin/env python3

from diagnosticism.contingent_reporting import abort
from diagnosticism.contingent_reporting import conrep
from diagnosticism.contingent_reporting import set_default_trailing_prompt

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

class Abort_tester(unittest.TestCase):

    def test_default(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            diagnosticism.set_program_name('myprog1')

            abort('over and out!', do_exit=False)

            self.assertEqual('myprog1: over and out!\n', fake_stderr.getvalue())

    def test_explicit_trailing_prompt(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            diagnosticism.set_program_name('myprog1')

            abort('over and out!', do_exit=False, trailing_prompt='get over yourself!')

            self.assertEqual('myprog1: over and out!; get over yourself!\n', fake_stderr.getvalue())

    def test_stock_trailing_prompt(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            diagnosticism.set_program_name('myprog1')

            abort('over and out!', do_exit=False, trailing_prompt=True)

            self.assertEqual('myprog1: over and out!; use --help for usage\n', fake_stderr.getvalue())

    def test_set_default_trailing_prompt(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            diagnosticism.set_program_name('myprog1')

            set_default_trailing_prompt('ok, now')

            abort('over and out!', do_exit=False, trailing_prompt=True)

            set_default_trailing_prompt(None)

            self.assertEqual('myprog1: over and out!; ok, now\n', fake_stderr.getvalue())

    def test_set_default_trailing_prompt(self):

        with patch('sys.stderr', new=StringIO()) as fake_stderr:

            diagnosticism.set_program_name('myprog1')

            set_default_trailing_prompt('ok, now')

            abort('over and out!', do_exit=False, trailing_prompt=False)

            set_default_trailing_prompt(None)

            self.assertEqual('myprog1: over and out!\n', fake_stderr.getvalue())



if '__main__' == __name__:

    unittest.main()



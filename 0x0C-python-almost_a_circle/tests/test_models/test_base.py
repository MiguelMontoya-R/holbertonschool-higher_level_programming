#!/usr/bin/python3
"""
test module
"""


import unittest
import pep8
from models.base import Base


class Test_base(unittest.TestCase):
    """
    class for testing Base class' methods
    """

    def test_pep8_conformance_base(self):
        """
        Test that base.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

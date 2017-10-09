"""
Includes tests for {{ cookiecutter.package_name }} module.
"""


# python setup.py test

from unittest import TestCase

import {{ cookiecutter.package_name }}


class Test1(TestCase):
    """
    Tests the class.
    """
    def test_say_the_word(self):
        """
        Tests the say_the_word() method.
        """
        expected = " Chips"
        actual = {{ cookiecutter.package_name }}.say_the_word()
        self.assertEqual(expected, actual)

from django.test import TestCase
from django.conf import settings

# Create your tests here.


def concate_two_strings(str1, str2):
    return str1 + str2


class TestExample(TestCase):
    def test_concate_two_strings(self):
        self.assertEqual(concate_two_strings("Hello, ", "How are you?"), "Hello, How are you?")

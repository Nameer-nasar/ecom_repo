from django.test import TestCase


def check(str1, str2):
    return str1 + str2


class test_string(TestCase):
    def check_assert(self):
        self.assertEquals(check("hi", "hello"), "hihello")
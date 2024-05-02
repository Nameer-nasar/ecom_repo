from django.test import TestCase

class testurl(TestCase):
    def home_test(self):
        result = self.client.get('/')
        self.assertEquals(result.status_code, 200)
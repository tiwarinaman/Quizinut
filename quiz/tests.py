from django.test import TestCase


class QuizTestCase(TestCase):
    def setUp(self):
        print("setup method is executing...")

    def test(self):
        print("test method is executing...")

    def tearDown(self):
        print("tearDown is executing...")

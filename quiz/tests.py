from django.test import TestCase

from .models import Quiz, Teacher


# Create your tests here.
# class QuizTestCase(TestCase):
#     def setUp(self):
#         t = Teacher()
#         Quiz.objects.create(teacher=t, quiz_name="unit tesing", total_question=10, added_question="2",
#                             total_marks=10,
#                             time_duration=5)
#
#     def test_quiz_create(self):
#         quiz_name = Quiz.objects.get(quiz="unit testing")
#         total_question = Quiz.objects.get(total_question=10)
#         self.assertEqual(quiz_name.create(), "quiz can create")
#         self.assertEqual(total_question.getTotalQuestion(), "can get total questions")

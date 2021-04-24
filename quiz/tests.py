from django.test import TestCase

from quiz.models import Quiz, Question, Result


class QuizTestCase(TestCase):
    def setUp(self):
        Quiz.objects.create(quiz_name="react", total_question=10, added_question=10, total_marks=20, time_duration=7)
        Quiz.objects.create(quiz_name="linux", total_question=8, added_question=8, total_marks=16, time_duration=4)

    def test_quiz_name(self):
        qs = Quiz.objects.all()
        self.assertEqual(qs.count(), 2)
        qz1 = Quiz.objects.get(quiz_name="react")
        qz2 = Quiz.objects.get(quiz_name="linux")
        self.assertEqual(qz1.get_quiz_name(), "react")
        self.assertEqual(qz2.get_quiz_name(), "linux")

    def test_total_questions(self):
        qs = Quiz.objects.all()
        self.assertEqual(qs.count(), 2)
        qz1 = Quiz.objects.get(quiz_name="react")
        qz2 = Quiz.objects.get(quiz_name="linux")
        self.assertEqual(qz1.get_total_questions(), 10)
        self.assertEqual(qz2.get_total_questions(), 8)

    def test_added_question(self):
        qs = Quiz.objects.all()
        self.assertEqual(qs.count(), 2)
        qz1 = Quiz.objects.get(quiz_name="react")
        qz2 = Quiz.objects.get(quiz_name="linux")
        self.assertEqual(qz1.get_added_question(), 10)
        self.assertEqual(qz2.get_added_question(), 8)


class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question="what is linux?", marks=2, option1="1", option2="2", option3="3", option4="4",
                                correct_answer='4')
        Question.objects.create(question="what is react?", marks=1, option1="framework", option2="js library",
                                option3="both 1 & 2", option4="none of the above", correct_answer='2')

    def test_question(self):
        qs = Question.objects.all()
        self.assertEqual(qs.count(), 2)
        q1 = Question.objects.get(question="what is linux?")
        q2 = Question.objects.get(question="what is react?")
        self.assertEqual(q1.get_question(), "what is linux?")
        self.assertEqual(q2.get_question(), "what is react?")

    def test_correct_answer(self):
        qs = Question.objects.all()
        self.assertEqual(qs.count(), 2)
        q1 = Question.objects.get(question="what is linux?")
        q2 = Question.objects.get(question="what is react?")
        self.assertEqual(q1.get_correct_answer(), '4')
        self.assertEqual(q2.get_correct_answer(), '2')


class ResultTestCase(TestCase):
    def setUp(self):
        Result.objects.create(student_marks=10, number_of_correct_answers=5, time_taken=12, number_of_attempts=2)
        Result.objects.create(student_marks=8, number_of_correct_answers=4, time_taken=10, number_of_attempts=1)

    def test_student_marks(self):
        qs = Result.objects.all()
        self.assertEqual(qs.count(), 2)
        rs1 = Result.objects.get(student_marks=10)
        rs2 = Result.objects.get(student_marks=8)
        self.assertEqual(rs1.get_student_marks(), 10)
        self.assertEqual(rs2.get_student_marks(), 8)

    def test_number_of_correct_answers(self):
        qs = Result.objects.all()
        self.assertEqual(qs.count(), 2)
        rs1 = Result.objects.get(student_marks=10)
        rs2 = Result.objects.get(student_marks=8)
        self.assertEqual(rs1.get_number_of_correct_answers(), 5)
        self.assertEqual(rs2.get_number_of_correct_answers(), 4)

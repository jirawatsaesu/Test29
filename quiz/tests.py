from django.urls import resolve
from django.test import TestCase
from quiz.models import Quiz


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class QuizPageTest(TestCase):

    def test_uses_quiz_page_template(self):
        response = self.client.get('/quiz/')
        self.assertTemplateUsed(response, 'quiz.html')


    def test_can_save_a_POST_request(self):
        self.client.post('/quiz/', data={'quiz': '2+2*0+1=1', 'answer': False})
        self.assertEqual(Quiz.objects.count(), 1)

        new_question = Quiz.objects.first()
        self.assertEqual(new_question.question, '2+2*0+1=1')
        self.assertEqual(new_question.answer, False)


    def test_redirects_after_POST(self):
        response = self.client.post('/quiz/', data={'quiz': '2+2*0+1=1', 'answer': False})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/quiz/')


class AnswerPageTest(TestCase):

    def test_uses_answer_page_template(self):
        response = self.client.get('/answer/')
        self.assertTemplateUsed(response, 'answer.html')


class QuizModelTest(TestCase):

    def test_create_and_saving_question(self):
        first_question = Quiz()
        first_question.question = '2+2*0+1=1'
        first_question.answer = False
        first_question.save()

        second_question = Quiz()
        second_question.question = 'Tomatoes is vegetable'
        second_question.answer = False
        second_question.save()

        saved_question = Quiz.objects.all()
        self.assertEqual(saved_question.count(), 2)

        first_saved_question = saved_question[0]
        second_saved_question = saved_question[1]
        self.assertEqual(first_saved_question.question, '2+2*0+1=1')
        self.assertEqual(first_saved_question.answer, False)
        self.assertEqual(second_saved_question.question, 'Tomatoes is vegetable')
        self.assertEqual(second_saved_question.answer, False)

    def test_answer_question_and_points_collect(self):
        first_question = Quiz()
        first_question.question = '2+2*0+1=1'
        first_question.answer = False
        first_question.wrong_ans = 0
        first_question.correct_ans = 0
        first_question.save()

        # 2 correct answer
        first_question.correct_ans += 1
        first_question.correct_ans += 1

        # 1 wrong answer
        first_question.wrong_ans += 1

        first_question.save()
        saved_question = Quiz.objects.first()

        self.assertEqual(saved_question.correct_ans, 2)
        self.assertEqual(saved_question.wrong_ans, 1)

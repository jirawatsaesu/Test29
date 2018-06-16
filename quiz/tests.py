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


class AnswerPageTest(TestCase):

    def test_uses_answer_page_template(self):
        response = self.client.get('/answer/')
        self.assertTemplateUsed(response, 'answer.html')


class QuizModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_question = Quiz()
        first_question.question = '2+2*0+1=1'
        first_question.save()

        second_question = Quiz()
        second_question.question = 'Tomatoes is vegetable'
        second_question.save()

        saved_items = Quiz.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.question, '2+2*0+1=1')
        self.assertEqual(second_saved_item.question, 'Tomatoes is vegetable')

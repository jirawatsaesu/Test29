from selenium import webdriver
import unittest
import time

class QuizTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_create_quiz(self):
        # Tom want to test other people knowledge about Math
        self.browser.get('http://localhost:8000/')
        quiz_link = self.browser.find_element_by_link_text('Quiz')
        self.assertEqual(quiz_link.get_attribute('href'), 'http://localhost:8000/quiz/')

        time.sleep(0.5)
        quiz_link.click()

        # Tom create quiz "2+2*0+1=1" and click "False"
        form = self.browser.find_element_by_id('quiz')
        inputbox = form.find_elements_by_tag_name('input')
        self.assertEqual(inputbox[0].get_attribute('name'), 'quiz')
        self.assertEqual(inputbox[1].get_attribute('value'), 'True')
        self.assertEqual(inputbox[2].get_attribute('value'), 'False')
        self.assertEqual(inputbox[3].get_attribute('value'), 'submit')

        time.sleep(0.5)
        inputbox[0].send_keys('2+2*0+1=1')

        time.sleep(0.5)
        inputbox[2].click()

        # Tom quit website
        time.sleep(0.5)
        self.browser.quit()

    def test_can_answer_a_quiz(self):
        # Jan see a test about Math on website
        self.browser.get('http://localhost:8000/')
        answer_link = self.browser.find_element_by_link_text('Answer')
        self.assertEqual(answer_link.get_attribute('href'), 'http://localhost:8000/answer/')

        time.sleep(0.5)
        answer_link.click()

        # Jan see quiz "2+2*0+1=1" She think this answer is True
        form = self.browser.find_element_by_id('quiz')
        inputbox = form.find_elements_by_tag_name('input')
        self.assertEqual(inputbox[0].get_attribute('value'), 'True')
        self.assertEqual(inputbox[1].get_attribute('value'), 'False')
        self.assertEqual(inputbox[2].get_attribute('value'), 'submit')

        time.sleep(0.5)
        inputbox[0].click()

        time.sleep(0.5)
        inputbox[2].click()

        # Jan quit website
        time.sleep(0.5)
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')

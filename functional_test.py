from selenium import webdriver
import unittest
import time

class QuizTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_a_quiz(self):
        # ทอมต้องการสร้างแบบทดสอบความรู้ทางคณิตศาสตร์บนเว็บไซต์
        self.browser.get('http://localhost:8000/')
        quiz_link = self.browser.find_element_by_link_text('Quiz')
        self.assertEqual(quiz_link.get_attribute('href'), 'http://localhost:8000/quiz/')

        # เขาเข้าหน้าเว็บสำหรับสร้างแบบทดสอบ
        time.sleep(0.5)
        quiz_link.click()

        # เขาเห็นช่องสำหรับสร้างคำถาม
        form = self.browser.find_element_by_id('quiz')
        inputbox = form.find_elements_by_tag_name('input')
        self.assertEqual(inputbox[0].get_attribute('name'), 'quiz')
        self.assertEqual(inputbox[1].get_attribute('value'), 'True')
        self.assertEqual(inputbox[2].get_attribute('value'), 'False')
        self.assertEqual(inputbox[3].get_attribute('value'), 'submit')

        # เขาสร้างแบบทดสอบ "2+2*0+1=1"
        time.sleep(0.5)
        inputbox[0].send_keys('2+2*0+1=1')

        # คำตอบที่ถูกต้องสำหรับข้อนี้คือ "False"
        time.sleep(0.5)
        inputbox[2].click()

        # เขากดยืนยันแบบทดสอบที่สร้างขึ้น
        time.sleep(0.5)
        inputbox[3].click()

        # เขาออกจากเว็บไซต์ไป
        time.sleep(0.5)
        self.browser.quit()

    def test_can_answer_a_quiz(self):
        # แจนต้องการทดสอบความรู้ของตน
        self.browser.get('http://localhost:8000/')
        answer_link = self.browser.find_element_by_link_text('Answer')
        self.assertEqual(answer_link.get_attribute('href'), 'http://localhost:8000/answer/')

        # เธอเข้าหน้าเว็บสำหรับตอบคำถาม
        time.sleep(0.5)
        answer_link.click()

        # เธอเห็นแบบทดสอบ "2+2*0+1=1"
        form = self.browser.find_elements_by_tag_name('form')
        inputbox = form[0].find_elements_by_tag_name('input')
        self.assertEqual(inputbox[0].get_attribute('value'), '1')
        self.assertEqual(inputbox[1].get_attribute('value'), 'True')
        self.assertEqual(inputbox[2].get_attribute('value'), 'False')
        self.assertEqual(inputbox[3].get_attribute('value'), 'submit')

        # เธอคิดว่าคำตอบที่ถูกต้องของข้อนี้คือ "True"
        time.sleep(0.5)
        inputbox[1].click()

        # เธอกดยืนยันเพื่อส่งคำตอบ
        time.sleep(0.5)
        inputbox[3].click()

        # เธอได้ออกจากเว็บไซต์ไป
        time.sleep(0.5)
        self.browser.quit()

    def test_can_see_a_result(self):
        # ทอมต้องการจะดูคะแนนแบบทดสอบ "2+2*0+1=1" ที่เขาสร้างขึ้น
        self.browser.get('http://localhost:8000/')
        answer_link = self.browser.find_element_by_link_text('Result')
        self.assertEqual(answer_link.get_attribute('href'), 'http://localhost:8000/result/')

        # เขาเข้าหน้าเว็บสำหรับดูคะแนน
        time.sleep(0.5)
        answer_link.click()

        # เขาเห็นคะแนนของคนที่ตอบถูก และตอบผิด
        table = self.browser.find_element_by_id('result')
        rows = table.find_elements_by_tag_name('tr')
        cols = rows[1].find_elements_by_tag_name('td')
        self.assertEqual(cols[0].text, '1.')
        self.assertEqual(cols[1].text, '2+2*0+1=1')
        self.assertEqual(cols[2].text, 'False')

        # เขาออกจากเว็บไซต์ไป
        time.sleep(0.5)
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')

import unittest
from selenium import webdriver
from django.test import TestCase
import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class MyTestCase(unittest.TestCase):
    def registerNewUser(self):
        fake = Faker()
        login = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password1')
        password2 = self.browser.find_element_by_id('id_password2')
        email = self.browser.find_element_by_id('id_email')
        button_register = self.browser.find_element_by_id('register_submit')

        new_user_login = fake.user_name()
        new_user_email = fake.email()
        new_user_password = 'TajneHasło123'

        login.send_keys(new_user_login)
        email.send_keys(new_user_email)
        password.send_keys(new_user_password)
        password2.send_keys(new_user_password)
        button_register.send_keys(Keys.ENTER)
        time.sleep(2)

        data = [new_user_login, new_user_password,  new_user_email]

        return data
    
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'C:\Users\Lidia\TestDjango\chromedriver.exe')

    def test_something(self):
        self.assertEqual(True, True)
        
    def test_register(self):
        self.browser.get('http://localhost:8000/register')
        self.registerNewUser()
        self.header_text = self.browser.find_elements_by_class_name('alert-success')[0]
        self.assertIn('Your account has been created!', self.header_text.text)
        
    def test_register_too_short_password(self):
        self.browser.get('http://localhost:8000/register/')

        fake = Faker()
        login = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password1')
        password2 = self.browser.find_element_by_id('id_password2')
        email = self.browser.find_element_by_id('id_email')
        button_register = self.browser.find_element_by_id('register_submit')

        new_user_login = fake.user_name()
        new_user_email = fake.email()
        new_user_password = 'Ta123'

        login.send_keys(new_user_login)
        email.send_keys(new_user_email)
        password.send_keys(new_user_password)
        password2.send_keys(new_user_password)
        button_register.send_keys(Keys.ENTER)
        time.sleep(2)

        self.header_text = self.browser.find_element_by_id('error_1_id_password2').find_element_by_tag_name('strong')
        self.assertIn('To hasło jest za krótkie. Musi zawierać co najmniej 8 znaków.', self.header_text.text)
        
    def test_login_success(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element(By.LINK_TEXT, "Login").click()
        self.browser.find_element(By.ID, "id_username").send_keys("ada")
        self.browser.find_element(By.ID, "id_password").send_keys("student12345")
        self.browser.find_element(By.CSS_SELECTOR, ".btn").click()

    def test_add_post(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element(By.LINK_TEXT, "Login").click()
        self.browser.find_element(By.ID, "id_username").send_keys("ada")
        self.browser.find_element(By.ID, "id_password").send_keys("student12345")
        self.browser.find_element(By.CSS_SELECTOR, ".btn").click()

        self.header_text = self.browser.find_element_by_link_text('New post').click()
        time.sleep(2)

        new_post = self.addNewPost()
        post_title = new_post[0]
        self.addQuestion()

            # self.header_text = self.browser.find_element_by_link_text('Strona główna').click()
            # time.sleep(2)

        self.header_text = self.browser.find_element_by_link_text('Home').click()
        time.sleep(2)

        self.header_text = self.browser.find_element_by_link_text(quiz_title).click()
        time.sleep(2)

        self.header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(quiz_title, self.header_text)
                         
    def test_login_page(self):
        self.browser.get('http://localhost:8000/login')
        self.header_text = self.browser.find_element_by_tag_name('legend').text
        self.assertIn('Log In', self.header_text)

    def test_register_page(self):
        self.browser.get('http://localhost:8000/register')
        self.header_text = self.browser.find_element_by_tag_name('legend').text
        self.assertIn('Join', self.header_text)    
   

    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()


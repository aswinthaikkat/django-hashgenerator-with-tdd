from django.test import TestCase
from .forms import HashForm
from .models import Hash
#from selenium import webdriver

# Create your tests here.


class UnitTestCase(TestCase):
    def test_1(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_form_valid(self):
        form = HashForm(data={'name': 'hello'})
        self.assertTrue(form.is_valid())

    def test_for_model(self):
        hash = Hash()
        hash.name = 'hello'
        hash.encoding = 'abcde'
        hash.save()
        load_hash = Hash.objects.get(encoding='abcde')
        self.assertEqual(hash.encoding, load_hash.encoding)


# class FunctionalTestCase(TestCase):
#     def setUp(self):
#         self.browser = webdriver.Firefox()

#     def test_homepage(self):
#         self.browser.get('http://127.0.0.1:8000/')
#         self.assertIn('install', self.browser.page_source)

#     def tearDown(self):
#         pass
#         # self.browser.quit()

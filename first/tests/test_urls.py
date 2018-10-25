from django.urls import reverse,resolve
from django.test import TestCase, Client, LiveServerTestCase
from django.utils import timezone
from first.models import fooditem
from django.contrib.auth.models import User

class Testurls:

    def test_detail_url(self):
        path = reverse('welcome')
        assert resolve(path).view_name == 'welcome'

    def test_about_url(self):
        path = reverse('about')
        assert resolve(path).view_name == 'about'

    def test_mess_url(self):
        path = reverse('mess_update')
        assert resolve(path).view_name == 'mess_update'

# class LogInTest(TestCase):
#
#     def setUp(self):
#         self.credentials = {
#             'username': 'testuser',
#             'password': 'secret'}
#         User.objects.create_user(**self.credentials)
#
#     def test_login(self):
#         response = self.client.post('/accounts/login/', self.credentials, follow=True)
#         self.assertTrue(response.context['User'].is_active)

from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User,AnonymousUser
from mixer.backend.django import mixer
from first.views import welcome
from first.models import fooditem
import pytest
from django.test import TestCase
@pytest.mark.django_db
class TestViews(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestViews,cls).setUpClass()
        mixer.blend('first.fooditem')
        cls.factory = RequestFactory()

    def test_view_welcome_authenticated(self):
        path = reverse('welcome')
        request = self.factory.get(path)
        request.user = mixer.blend(User)

        response = welcome(request,pk=1)
        assert response.status_code == 200

    def test_view_welcome_unauthenticated(self):
        path = reverse('welcome')
        request = self.factory.get(path)
        request.user = AnonymousUser()

        response = welcome(request,pk=1)
        assert 'accounts/login' in response.url
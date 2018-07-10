
# Create your tests here.
from django.urls import reverse, include, path
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class AccountsTest(APITestCase):
    urlpatterns = [
        path('api/', include('accounts.urls')),
    ]   


    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }
        url = reverse('account-create')
        response = self.client.post(url, data, format='json')

        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 3)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

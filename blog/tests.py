from django.test import TestCase,Client
from django.contrib.auth.models import User
from blog.models import Blogpost
from django.urls import reverse

# Create your tests here.
class BlogpostViewTest(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
            )
        Blogpost.objects.create(title='Test Post 1', user=self.user, body='This is the body of test post 1')
        Blogpost.objects.create(title='Test Post 2', user=self.user, body='This is the body of test post 2')
        
        self.client=Client()
        self.url=reverse('blog')

    def test_get(self):
        response=self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        data=response.context['posts']
        self.assertEqual(len(data),2)
        self.assertEqual(data[0],{
            'id':1,
            'title':'Test Post 1',
            'author':self.user.username
        })
        self.assertEqual(data[1],{
            'id':2,
            'title':'Test Post 2',
            'author':self.user.username
        })

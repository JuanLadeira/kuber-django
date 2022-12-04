from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTestCase(TestCase):

    def setUp(self):
        Post.objects.create(title="Hello world")
        

    def test_failure(self):
        queryset = Post.objects.all()
        self.assertTrue(queryset.exists())
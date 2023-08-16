from django.test import TestCase, RequestFactory
from restaurant import views, models
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    def setUp(self):
        self.test_menu = models.Menu.objects.all()
        self.factory = RequestFactory()
        self.user = User

    def test_getall(self):
        request = self.factory.get('/restaurant/menu')
        response = views.MenuItemView.as_view()(request)
        print(response)
        self.assertEqual(response.status_code, 200)

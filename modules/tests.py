from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from modules.models import Module
from users.models import User


class ModuleTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False
        )
        self.user.set_password('test')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.module = Module.objects.create(
            title='Test module',
            owner=self.user
        )

    def test_create_module(self):
        """Тестирование создания модуля"""

        data = {
            'title': 'Test module',
            'owner': self.user.pk
        }

        response = self.client.post('/modules/create/', data=data)

        print(response.json())

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Module.objects.all().count(), 2)

    def test_list_modules(self):
        """Тестирование вывода списка модулей"""

        response = self.client.get('/modules/')
        print(response.json())

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json()['results'],
            [
                {
                    'id': self.module.id,
                    'title': 'Test module',
                    'description': None,
                    'owner': self.user.pk,
                }
            ]
        )

    def test_update_module(self):
        """Тестирование изменения модуля"""

        change_data = {
            'title': 'title_update',
        }
        response = self.client.patch(f'/modules/update/{self.module.id}/', data=change_data)
        self.maxDiff = None

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(),
            {
                'id': self.module.id,
                'title': 'title_update',
                'description': None,
                'owner': self.user.pk,
            }
        )

    def test_delete_module(self):
        """Тестирование удаления модуля"""

        data = {
            'title': 'Test module',
            'owner': self.user.pk
        }

        posted = self.client.post(reverse('modules:module-create'), data, format='json')
        response = self.client.delete(reverse('modules:module-delete', kwargs={'pk': posted.json()['id']}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

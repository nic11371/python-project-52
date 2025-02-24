from django.test import TestCase
from task_manager.user.models import CustomUser
from django.urls import reverse


class UserCustomTestCase(TestCase):

    def setUp(self):
        CustomUser.objects.create(
            first_name='Ivan',
            last_name='Grozniy',
            username='IvGroz',
            password1='Test123@#',
            password2='Test123@#'
        )
        CustomUser.objects.create(
            first_name='Mariya',
            last_name='Petrova',
            username='Masha003',
            password1='Te1@',
            password2='Te1@'
        )

    def test_signUp(self):
        resp = self.client.get(reverse('user_create'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='users/create.html')

        resp = self.client.post(reverse('user_create'), {
            'first_name': 'Nikolay',
            'last_name': 'Melnikov',
            'username': 'nic',
            'password1': 'Test123@#',
            'password2': 'Test123@#',
        })
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        user = CustomUser.objects.last()
        self.assertEqual(user.first_name, 'Nikolay')
        self.assertEqual(user.last_name, 'Melnikov')
        self.assertEqual(user.username, 'nic')

        resp = self.client.get(reverse('users'))
        self.assertTrue(len(resp.context['users']) == 3)

    def test_ListUsers(self):
        resp = self.client.get(reverse('users'))
        self.assertTrue(len(resp.context['users']) == 2)

    def test_UpdateUser(self):
        user = CustomUser.objects.get(id=1)
        # resp = self.client.get(
        #     reverse('user_update', kwargs={'pk': user.id})
        # )
        # self.assertEqual(resp.status_code, 302)
        # self.assertRedirects(resp, reverse('login'))
        self.client.force_login(user)
        resp = self.client.get(
            reverse('user_update', kwargs={'pk': user.id})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='users/update.html')
        resp = self.client.post(
            reverse('user_update', kwargs={'pk': user.id}),
            {
                'first_name': 'Petya',
                'last_name': 'Piter',
                'username': 'Petr1',
                'password1': 'Te1@',
                'password2': 'Te1@',
            }
        )
        self.assertEqual(resp.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Petya')

    def test_DeleteUser(self):
        user = CustomUser.objects.get(id=2)
        # resp = self.client.get(
        #     reverse('user_delete', kwargs={'pk': user.id})
        # )
        # self.assertEqual(resp.status_code, 302)
        # self.assertRedirects(resp, reverse('login'))
        self.client.force_login(user)
        resp = self.client.get(
            reverse('user_delete', kwargs={'pk': user.id})
        )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(
            reverse('user_delete', kwargs={'pk': user.id})
        )
        self.assertRedirects(resp, reverse('users'))
        self.assertEqual(resp.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(CustomUser.objects.count(), 0)

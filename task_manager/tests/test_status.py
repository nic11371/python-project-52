from django.test import TestCase
from task_manager.status.models import CustomStatus
from task_manager.user.models import CustomUser
from django.urls import reverse


class StatusCustomTestCase(TestCase):
    fixtures = ["status_test"]

    def login(self):
        user = CustomUser.objects.get(id=1)
        self.client.force_login(user)

    def test_ListStatuses(self):
        self.login()
        resp = self.client.get(reverse('statuses'))
        self.assertTrue(len(resp.context['statuses']) == 2)

    def test_create_status(self):
        self.login()
        resp = self.client.get(reverse('status_create'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='statuses/create.html')

        resp = self.client.post(reverse('status_create'), {
            'status_name': 'test',
        })
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('statuses'))
        status = CustomStatus.objects.last()
        self.assertEqual(status.status_name, 'test')

        resp = self.client.get(reverse('statuses'))
        self.assertTrue(len(resp.context['statuses']) == 3)

    def test_UpdateStatus(self):
        self.login()
        status = CustomStatus.objects.get(id=1)
        resp = self.client.get(
            reverse('status_update', kwargs={'pk': status.id})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='statuses/update')
        resp = self.client.post(
            reverse('status_update', kwargs={'pk': status.id}), {
                'status_name': 'test_status'
            })
        self.assertEqual(resp.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.status_name, 'test_status')

    def test_DeleteStatus(self):
        self.login()
        status = CustomStatus.objects.get(status_name="welcome")
        resp = self.client.get(
            reverse('status_delete', kwargs={'pk': status.id})
        )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(
            reverse('status_delete', kwargs={'pk': status.id})
        )
        self.assertRedirects(resp, reverse('statuses'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(CustomStatus.objects.count(), 1)

from django.test import TestCase
from task_manager.label.models import Label
from task_manager.user.models import User
from django.urls import reverse


class LabelTestCase(TestCase):
    fixtures = ["label_test"]

    def login(self):
        user = User.objects.get(id=1)
        self.client.force_login(user)

    def test_ListLabels(self):
        self.login()
        resp = self.client.get(reverse('labels'))
        self.assertTrue(len(resp.context['labels']) == 2)

    def test_create_label(self):
        self.login()
        resp = self.client.get(reverse('label_create'))
        self.assertEqual(resp.label_code, 200)
        self.assertTemplateUsed(resp, template_name='labels/create.html')

        resp = self.client.post(reverse('label_create'), {
            'label_name': 'test',
        })
        self.assertEqual(resp.label_code, 302)
        self.assertRedirects(resp, reverse('labels'))
        label = Label.objects.last()
        self.assertEqual(label.name, 'test')

        resp = self.client.get(reverse('labels'))
        self.assertTrue(len(resp.context['labels']) == 3)

    def test_UpdateLabel(self):
        self.login()
        label = Label.objects.get(id=1)
        resp = self.client.get(
            reverse('label_update', kwargs={'pk': label.id})
        )
        self.assertEqual(resp.label_code, 200)
        self.assertTemplateUsed(resp, template_name='labels/update')
        resp = self.client.post(
            reverse('label_update', kwargs={'pk': label.id}), {
                'label_name': 'test_label'
            })
        self.assertEqual(resp.label_code, 302)
        label.refresh_from_db()
        self.assertEqual(label.name, 'test_label')

    def test_DeleteLabel(self):
        self.login()
        label = Label.objects.get(label_name="welcome")
        resp = self.client.get(
            reverse('label_delete', kwargs={'pk': label.id})
        )
        self.assertEqual(resp.label_code, 200)
        resp = self.client.post(
            reverse('label_delete', kwargs={'pk': label.id})
        )
        self.assertRedirects(resp, reverse('labels'))
        self.assertEqual(resp.label_code, 302)
        self.assertEqual(Label.objects.count(), 1)

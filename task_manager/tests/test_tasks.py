from django.test import TestCase
from task_manager.task.models import Task
from django.urls import reverse


class taskCustomTestCase(TestCase):
    fixtures = ["task_test"]

    def test_TaskCreate(self):
        resp = self.client.get(reverse('task_create'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='tasks/create.html')

        resp = self.client.post(reverse('task_create'), {
            'task_name': 'Nikolay',
            'status': 'online',
            'author': 'nic',
            'executor': 'home',
            'description': 'My first project',
        })
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        task = Task.objects.last()
        self.assertEqual(task.task_name, 'Nikolay')
        self.assertEqual(task.status, 'online')
        self.assertEqual(task.author, 'nic')

        resp = self.client.get(reverse('tasks'))
        self.assertTrue(len(resp.context['tasks']) == 3)

    def test_ListTasks(self):
        resp = self.client.get(reverse('tasks'))
        self.assertTrue(len(resp.context['tasks']) == 2)

    def test_UpdateTask(self):
        task = Task.objects.get(id=1)
        # resp = self.client.get(
        #     reverse('task_update', kwargs={'pk': task.id})
        # )
        # self.assertEqual(resp.status_code, 302)
        # self.assertRedirects(resp, reverse('login'))
        self.client.force_login(task)
        resp = self.client.get(
            reverse('task_update', kwargs={'pk': task.id})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='tasks/update.html')
        resp = self.client.post(
            reverse('task_update', kwargs={'pk': task.id}),
            {
                'task_name': 'Nasty',
                'status': 'offline',
                'author': 'nas',
                'executor': 'work',
                'description': 'My second project',
            }
        )
        self.assertEqual(resp.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.task_name, 'Nasty')

    def test_DeleteTask(self):
        task = Task.objects.get(task_name="Nasty")
        # resp = self.client.get(
        #     reverse('task_delete', kwargs={'pk': task.id})
        # )
        # self.assertEqual(resp.status_code, 302)
        # self.assertRedirects(resp, reverse('login'))
        self.client.force_login(task)
        resp = self.client.get(
            reverse('task_delete', kwargs={'pk': task.id})
        )
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post(
            reverse('task_delete', kwargs={'pk': task.id})
        )
        self.assertRedirects(resp, reverse('tasks'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

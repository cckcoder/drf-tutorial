from django.test import TestCase

from api.models import Task


class TaskTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(
            title="This task for test", description="foo bar test test 1234", completed=False
        )

    def test_task_content(self):
        self.assertEqual(self.task.title, "This task for test")
        self.assertEqual(self.task.description, "foo bar test test 1234")
        self.assertFalse(self.task.completed)

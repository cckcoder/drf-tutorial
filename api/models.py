from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.title

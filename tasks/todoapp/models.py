from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200,  default="Task")
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['complete']

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_todo',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=55
    )
    description = models.TextField(
        blank=True, null=True
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    date = models.DateField()

    def __str__(self):
        return self.title

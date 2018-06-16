from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.TextField()
    answer = models.BooleanField(default=True)

    def __str__(self):
        return self.question

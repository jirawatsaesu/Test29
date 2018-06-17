from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.TextField()
    answer = models.BooleanField(default=True)
    correct_ans = models.PositiveIntegerField(default=0)
    wrong_ans = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question

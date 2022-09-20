from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id) + '.    ' + self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    # question = models.CharField(max_length=150)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.question.id) + ' ' + str(self.id) + ' ' + self.choice_text



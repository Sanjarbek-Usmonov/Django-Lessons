from statistics import mode
from django.db import models
from django.core.validators import EmailValidator, RegexValidator

class User(models.Model):
    user = models.CharField(max_length=150)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ManyToManyField(User)

    def __str__(self) -> str:
        return str(self.id) + '.    ' + self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    # question = models.CharField(max_length=150)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.question.id) + ' ' + str(self.id) + ' ' + self.choice_text

class Info(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?998?\d{9,13}$', message='Phone number must be entered in the format: "+999999999". Up to 14 digits allowed.')
    name = models.CharField(max_length=150, null=True, blank=True)

    mobile = models.CharField(max_length=13, null=True, validators=[phone_regex], unique=True)

    email = models.EmailField(null=True, blank=True, validators=[EmailValidator(message="Invalid Email")], unique=True)

    def __str__(self) -> str:
        return self.name

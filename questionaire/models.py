from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
	Question_text = models.CharField(max_length=120)
	user          = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.Question_text

class MultipleChoices(models.Model):
	question    = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes       = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

class TextAnswer(models.Model):
	question    = models.ForeignKey(Question,on_delete=models.CASCADE)
	answer      = models.CharField(max_length=200)
	def __str__(self):
		return self.answer
class File(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    file     = models.FileField(upload_to='static_cdn')
    def __str__(self):
    	return self.file.name
class CheckBox(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	checkbox = models.CharField(max_length=120)
	def __str__(self):
		return self.checkbox
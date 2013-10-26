from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Basicuser(models.Model):
	user			= models.OneToOneField(User)
	birthday		= models.DateField()
	ispremium	= models.CharField(max_length=1, choices=(('0', 'no'),('1', 'yes'),('2', 'Pending Approval')))
	county		= models.CharField(max_length=50)	
	
	def __unicode__(self):
		return self.name
		
class Premiumuser(models.Model):
	user			= models.OneToOneField(User)
	address		= models.CharField(max_length=200)	
	city			= models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name
		
#create user object to attach to our news app

def create_news_user_callback(sender, instance, **kwargs):
	news, new = News.objects.get_or_create(user=instance)
post_save.connect(create_news_user_callback, User)


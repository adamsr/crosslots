from django.db import models

NEWS_CATEGORIES = (
	('H', 'Health'),
	('E', 'Entertainment'),
	('T', 'Tech'),
	('L', 'Living'),
	('H', 'Humor'),
	('T', 'Travel'),
	('M', 'Money'),
)

# Create your models here.
class News(models.Model):
	title		= models.CharField(max_length=200)
	slug		= models.SlugField(unique=True)
	content	= models.TextField(blank=True)
	category	= models.CharField(max_length=1, choices=NEWS_CATEGORIES)
	
	def __unicode__(self):
		return self.title
	
class Scores(models.Model):
	team_win		= models.CharField(max_length=200)
	win_score	= models.CharField(max_length=5)
	team_lose	= models.CharField(max_length=200)
	lose_score	= models.CharField(max_length=5)
	
	def __unicode__(self):
		return self.team_win
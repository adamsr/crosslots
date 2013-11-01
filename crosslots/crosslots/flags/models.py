from django.db import models
from news.models import *
from scores.models import Scores
# Create your models here.

NEWSFLAGS = (
	('1', 'Inapropriate Content'),
	('2', 'Plaigarism'),
	('3', 'Inaccurate'),
	)

class NewsFlags(models.Model):
	flagged_news = models.ForeignKey(News)
	explanation = models.CharField(max_length = 1, choices=NEWSFLAGS)
	comments = models.CharField(max_length = 500)
	
class ScoresFlags(models.Model):
	flagged_scores = models.ForeignKey(Scores)
	comments = models.CharField(max_length = 500)
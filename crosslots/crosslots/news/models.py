from django.db import models
from organizations.models import Organizations
from county.models import County

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
	content	= models.TextField()
	category	= models.CharField(max_length=1, choices=NEWS_CATEGORIES, blank=True)
	news_orgs = models.ManyToManyField(Organizations, blank=True)
	news_county = models.ManyToManyField(County, blank=False)
	
	def __unicode__(self):
		return self.title
	

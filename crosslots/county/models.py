from django.db import models

STATES = (
	('MO', 'Missouri'),
	('AR', 'Arkansas'),
	('KS', 'Kansas'),
)

# Create your models here.
class County(models.Model):
	county_name = models.CharField(max_length=200)
	county_state = models.CharField(max_length=2, choices=STATES)
	
	def __unicode__(self):
		return self.county_name
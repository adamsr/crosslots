from django.db import models
from county.models import County
from clauth.models import CustomUser

# Create your models here.

class OrgType(models.Model):
	org_type = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.org_type

class Organizations(models.Model):
	org_name = models.CharField(max_length=200)
	org_admin = models.ManyToManyField(CustomUser)
	org_phone = models.CharField(max_length=10)
	org_county = models.ForeignKey(County)
	org_type = models.ForeignKey(OrgType)
	sub_org = models.ForeignKey('self', null=True, blank=True)
	def __unicode__(self):
		return self.org_name
		
class PremiumOrganizations(models.Model):
	org = models.OneToOneField(Organizations)
	org_logo = models.ImageField(upload_to = 'pic_folder/')
	org_web = models.CharField(max_length=500)
	org_facebook = models.CharField(max_length=200)
	org_twitter = models.CharField(max_length=200)
from django.db import models
from organizations.models import Organizations
from clauth.models import CustomUser

# Create your models here.
class UserOrgConnections(models.Model):
	user = models.ForeignKey(CustomUser)
	orgs = models.ForeignKey(Organizations)
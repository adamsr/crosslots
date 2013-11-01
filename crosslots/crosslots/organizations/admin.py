from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from clauth.models import CustomUser
from organizations.models import Organizations, OrgType, PremiumOrganizations

admin.site.register(Organizations)
admin.site.register(OrgType)
admin.site.register(PremiumOrganizations)

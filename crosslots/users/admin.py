from django.contrib import admin
from users.models import Basicuser
from users.models import Premiumuser

admin.site.register(Basicuser)
admin.site.register(Premiumuser)
from django.contrib import admin
from flags.models import NewsFlags, ScoresFlags

admin.site.register(NewsFlags)
admin.site.register(ScoresFlags)
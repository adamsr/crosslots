from django.contrib import admin
from news.models import News, Scores

class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ['title','content',]
	
admin.site.register(News, NewsAdmin)
admin.site.register(Scores)
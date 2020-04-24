from django.contrib import admin

# Register your models here.
from .models import NewsArticle

class NewsArticleAdmin(admin.ModelAdmin):
    model = NewsArticle 


admin.site.register(NewsArticle, NewsArticleAdmin)

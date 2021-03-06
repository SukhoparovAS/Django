from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Article, Category, Comment, Profile, LikedArticle
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


admin.site.register(Article, ArticleAdmin)


admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(LikedArticle)

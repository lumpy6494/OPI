from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_on_top = True
    list_display = ( 'id', 'title','category', 'author', 'created_at', 'views', 'slug','get_photo')
    list_display_links = ('id','title',)
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title',)
    list_filter = ('category','tags')
    readonly_fields = ('views','created_at', 'get_photo')
    fields =('title', 'slug', 'category', 'content','photo', 'author','tags', 'created_at', 'views', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="55">')
        return '-'

    get_photo.short_description = 'Фото'


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Tag, TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)

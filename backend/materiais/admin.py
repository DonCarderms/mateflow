from django.contrib import admin

# Register your models here.
from.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'active', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'material', 'comment', 'created_at', 'updated_at')
    search_fields = ('comment',)

admin.site.register(User,UserAdmin)
admin.site.register(Material,MaterialAdmin)
admin.site.register(Comment,CommentAdmin)

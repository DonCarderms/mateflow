from django.contrib import admin

# Register your models here.
from.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'last_login', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'gender')
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'active', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('user', 'active')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','user', 'material', 'created_at', 'updated_at')
    search_fields = ('comment',)
    list_filter = ('user', 'material')


admin.site.register(User,UserAdmin)
admin.site.register(Material,MaterialAdmin)
admin.site.register(Comment,CommentAdmin)

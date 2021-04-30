from django.contrib import admin
from .models import Post, Comment, Profile, Contactus


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technology')
    list_filter = ('technology',)
    search_fields = ['title', 'technology']


class ContactusAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contactus, ContactusAdmin)

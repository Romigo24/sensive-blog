from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display= ('title', 'published_at', 'author')
    raw_id_fields = ('author', 'likes', 'tags')


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post')
    raw_id_fields = ('post', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
# admin.site.register(Post)
# admin.site.register(Tag)
# admin.site.register(Comment)

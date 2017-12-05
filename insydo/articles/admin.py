from django.contrib import admin
from articles.models import Category,Article
from lock_tokens.admin import LockableModelAdmin
# Register your models here.




# class ArticleAdmin(admin.ModelAdmin):
#
#     def get_readonly_fields(self, request, obj=None):
#         # make all fields readonly
#         readonly_fields = list(set(
#             [field.name for field in self.opts.local_fields] +
#             [field.name for field in self.opts.local_many_to_many]
#         ))
#         if 'is_submitted' in readonly_fields:
#             readonly_fields.remove('is_submitted')
#         return readonly_fields

class MyModelAdmin(LockableModelAdmin):
    pass


admin.site.register(Article, MyModelAdmin)
admin.site.register(Category,MyModelAdmin)
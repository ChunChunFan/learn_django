from django.contrib import admin

from backend.models import User,Contact,Tag

# Register your models here.
# 内嵌关联
class TagInline(admin.TabularInline):
    model = Tag

# 修改默认的ADD页面
class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')
    list_display = ('name','age', 'email') # 列表页显示的行
    search_fields = ('name',) # 搜索条件
    inlines = [TagInline]  # 内嵌关联
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
# admin.site.register([User, Tag])
admin.site.register(User)

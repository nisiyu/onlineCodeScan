from django.contrib import admin
from .models import user, plan, item
# Register your models here.

class PlanInline(admin.StackedInline):
    model = plan
    extra = 3

class UserAdmin(admin.ModelAdmin):
    #list_display = ['usernmae']
    list_display = ['username']
    fieldsets = [
        (None, {'fields': ['username']}),
        ('Date Infortion', {'fields': ['password'], 'classes': ['collapse']}),
    ]
    inlines = [PlanInline]

admin.site.register(user, UserAdmin)
#admin.site.register(plan)
admin.site.register(item)
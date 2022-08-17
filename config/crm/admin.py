from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from users.models import User
# Register your models here.
from .models import User, Clients, Orders, Service, Department, ProjectService


class ProjectServiceInline(admin.TabularInline):
    model = ProjectService
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = (ProjectServiceInline,)


class ServiceAdmin(admin.ModelAdmin):
    inlines = (ProjectServiceInline,)


admin.site.register(Clients),
admin.site.register(Orders, OrderAdmin),
admin.site.register(Service, ServiceAdmin),
admin.site.register(Department),
admin.site.register(ProjectService),


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role'),
        }),
    )

    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]['fields'] = ('first_name', 'last_name',)

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

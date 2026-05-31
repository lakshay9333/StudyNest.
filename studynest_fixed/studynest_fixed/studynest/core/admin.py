from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils import timezone as dj_tz
from .models import User, FriendRequest, Message, Task, FocusSession


def local_time(obj, field='created_at'):
    """Return field value converted to local timezone."""
    val = getattr(obj, field, None)
    if val is None:
        return '-'
    return dj_tz.localtime(val).strftime('%Y-%m-%d %H:%M:%S %Z')


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display  = ('username', 'student_id', 'email', 'first_name', 'last_name', 'is_staff', 'joined_local')
    search_fields = ('username', 'student_id', 'email')
    fieldsets     = BaseUserAdmin.fieldsets + (
        ('StudyNest', {'fields': ('student_id', 'color')}),
    )

    @admin.display(description='Joined (IST)', ordering='created_at')
    def joined_local(self, obj):
        return local_time(obj, 'created_at')


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display  = ('sender', 'receiver', 'status', 'sent_local')
    list_filter   = ('status',)
    search_fields = ('sender__username', 'receiver__username')

    @admin.display(description='Sent At (IST)', ordering='created_at')
    def sent_local(self, obj):
        return local_time(obj, 'created_at')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display    = ('sender', 'receiver', 'text', 'sent_local')
    search_fields   = ('sender__username', 'receiver__username', 'text')
    readonly_fields = ('created_at',)

    @admin.display(description='Sent At (IST)', ordering='created_at')
    def sent_local(self, obj):
        return local_time(obj, 'created_at')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display  = ('user', 'text', 'priority', 'done', 'created_local')
    list_filter   = ('priority', 'done')
    search_fields = ('user__username', 'text')

    @admin.display(description='Created (IST)', ordering='created_at')
    def created_local(self, obj):
        return local_time(obj, 'created_at')


@admin.register(FocusSession)
class FocusSessionAdmin(admin.ModelAdmin):
    list_display  = ('user', 'mode', 'duration_mins', 'completed_local')
    list_filter   = ('mode',)
    search_fields = ('user__username',)

    @admin.display(description='Completed At (IST)', ordering='completed_at')
    def completed_local(self, obj):
        return local_time(obj, 'completed_at')

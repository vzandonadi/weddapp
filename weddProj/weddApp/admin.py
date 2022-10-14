from django.contrib import admin
from weddApp.models import Guests, Groups, GroupMsg, IndividualMsg, Confirmed, AppVersion, PushToken
# Register your models here.
# admin.site.register(Guests)

class GroupsAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'description_group')

class GuestsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'midle_name', 'last_name', 'whatsapp_number', 'is_godparents','is_confirmed', 'group_belongs')
    list_filter = ('is_confirmed','is_godparents', 'group_belongs')
    fields = ['whatsapp_number', 'first_name', 'midle_name', 'last_name', ('is_godparents','group_belongs') ,'is_confirmed']
    search_fields = ('first_name','last_name','whatsapp_number', 'group_belongs')

class GroupMsgAdmin(admin.ModelAdmin):
    list_display = ('msg_from', 'msg_to', 'msg_type', 'msg_subject')
    list_filter = ('msg_from', 'msg_to', 'msg_type',)
    search_fields = ('msg_from', 'msg_to', 'msg_type', 'msg_subject')

class IndividualMsgAdmin(admin.ModelAdmin):
    list_display = ('msg_from', 'msg_to', 'msg_type', 'msg_subject')
    list_filter = ('msg_from', 'msg_to', 'msg_type',)
    search_fields = ('msg_from', 'msg_to', 'msg_type', 'msg_subject')

class ConfirmedAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'relationship', 'who_confirmed', 'group_belongs')
    list_filter = ('first_name', 'last_name', 'who_confirmed', 'group_belongs')
    search_fields = ('first_name', 'last_name', 'relationship', 'who_confirmed', 'group_belongs')

class AppVersionAdmin(admin.ModelAdmin):
    list_display = ('version','version_description','released_date')
    list_filter = ('version','released_date')
    search_fields = ('version','released_date')

class PushTokenAdmin(admin.ModelAdmin):
    list_display = ('guest', 'token', 'created_date')
    list_filter = ('guest', 'created_date')
    search_fields = ('guest', 'token', 'created_date')

admin.site.register(Groups, GroupsAdmin)
admin.site.register(Guests, GuestsAdmin)
admin.site.register(GroupMsg, GroupMsgAdmin)
admin.site.register(IndividualMsg, IndividualMsgAdmin)
admin.site.register(Confirmed, ConfirmedAdmin)
admin.site.register(AppVersion, AppVersionAdmin)
admin.site.register(PushToken, PushTokenAdmin)

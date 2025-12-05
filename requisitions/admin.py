from django.contrib import admin
from .models import UserProfile, Requisition, LineItem, ApprovalLog

admin.site.register(UserProfile)
admin.site.register(Requisition)
admin.site.register(LineItem)
admin.site.register(ApprovalLog)


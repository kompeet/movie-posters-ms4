from django.contrib import admin
from .models import SendBack


@admin.register(SendBack)
class SendBackAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'reason',
        'email',
        'order_number',
    )

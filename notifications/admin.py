from django.contrib import admin
from .models import AppointmentNotification
from django.utils import timezone

class AppointmentNotificationAdmin(admin.ModelAdmin):
    list_display = ('id','appointment', 'get_doctor', 'get_patient', 'get_hospital', 'notification_type', 'is_read', 'created_at')
    list_filter = ('is_read', 'notification_type', 'created_at')
    search_fields = ('appointment__patient__name', 'appointment__doctor__name', 'appointment__hospital__name', 'message')
    readonly_fields = ('created_at', 'read_at')
    actions = ['mark_as_read']

    def get_queryset(self, request):
        """Optimize query by selecting related fields."""
        qs = super().get_queryset(request)
        return qs.select_related('appointment__doctor', 'appointment__patient', 'appointment__hospital')

    def get_doctor(self, obj):
        """Display the doctor associated with the appointment."""
        return f'{obj.appointment.doctor.user.first_name} {obj.appointment.doctor.user.last_name}'
    get_doctor.short_description = 'Doctor'

    def get_patient(self, obj):
        """Display the patient associated with the appointment."""
        return f'{obj.appointment.doctor.user.username}'
    get_patient.short_description = 'Patient'

    def get_hospital(self, obj):
        """Display the hospital associated with the appointment."""
        return obj.appointment.hospital.name
    get_hospital.short_description = 'Hospital'

    def mark_as_read(self, request, queryset):
        """Custom action to mark selected notifications as read."""
        updated = queryset.update(is_read=True, read_at=timezone.now())
        self.message_user(request, f"{updated} notification(s) marked as read.")
    mark_as_read.short_description = "Mark selected notifications as read"

# Register the admin class with the model
admin.site.register(AppointmentNotification, AppointmentNotificationAdmin)

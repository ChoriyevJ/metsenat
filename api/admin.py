from django.contrib import admin
from api import models


@admin.register(models.HTI)
class HTIAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'sponsorship_sum', 'spent_sum',
                    'date', 'status', 'person_type', 'actions']
    list_editable = ['status', 'person_type', 'actions']
    list_filter = ['date', 'status']
    search_fields = ['last_name', 'first_name']

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'student_type', 'contract_amount', 'actions']
    list_editable = ['student_type', 'actions']
    list_filter = ['allocated_sum', 'student_type']
    search_fields = ['last_name', 'first_name']


admin.site.register(models.SponsorForStudent)



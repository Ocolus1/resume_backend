from django.contrib import admin
from .models import ResumeProfile, EmploymentHistory, Education, Website, Skills

# Register your models here.
admin.site.register(ResumeProfile)
admin.site.register(EmploymentHistory)
admin.site.register(Education)
admin.site.register(Website)
admin.site.register(Skills)
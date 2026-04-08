from django.contrib import admin
from deploy_app.models import employee
class emp_admin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','emp_salary']
    ordering=['emp_id']
admin.site.register(employee,emp_admin)
# Register your models here.

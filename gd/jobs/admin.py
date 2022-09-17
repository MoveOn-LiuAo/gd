from django.contrib import admin
from jobs.models import Job

# Register your models here.

#管理属性
class JobAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date') #隐藏列表
    list_display = ('job_name','job_city','creator','created_date','modified_date')  #展示列表

    def save_model(self, request, obj, form, change):     #提交前默认保存
        obj.creator = request.user
        super().save_model(request,obj,form,change)

admin.site.register(Job,JobAdmin)   #注册Job
from django.contrib import admin

# Register your models here.

from .models import User,Role,Feature,UserFlow,Security    

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Feature)
admin.site.register(UserFlow)
admin.site.register(Security)

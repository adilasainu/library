from django.contrib import admin

# Register your models here.

# from users.models import Users
from users.models import CustomUser,Users

# Register your models here.

admin.site.register(Users)
admin.site.register(CustomUser)

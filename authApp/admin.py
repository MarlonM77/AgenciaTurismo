from django.contrib import admin

from authApp.models.plan import Plan
from .models.user   import User


admin.site.register(User)
admin.site.register(Plan)
from django.contrib import admin
from profiles_app import models

# Allows django admin to register UserProfile model with admin site
admin.site.register(models.UserProfile)
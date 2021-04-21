from django.contrib import admin
from profilesAPI import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
from django.contrib import admin
from .models import Lead, Agent, User, Profile
# Register your models here.

admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(User)
admin.site.register(Profile)


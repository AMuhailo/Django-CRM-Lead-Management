from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

#Custom user
class User(AbstractUser):
    is_organisation = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    
#Present client
class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank = True, null = True)
    phone = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name='organisation_leads')
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL, related_name = 'leads')
    class Meta:
        ordering = ['-id','age']
    
    def get_absolute_url(self):
        return reverse("lead:lead_detail_url", args=[self.pk])
    
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    
# Agent who work with Lead
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Profile, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("agent:agent_detail_url", args=[self.pk])
    
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
   id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
   name = models.CharField(max_length=100, null=True)
   email = models.EmailField(unique=True)
   bio = models.TextField(null=True, blank=True)
   is_participant = models.BooleanField(default=True, null=True)
   avatar = models.ImageField(default="default.png")
   
   USERNAME_FIELD = "email"
   REQUIRED_FIELDS = ["username"]

class Event(models.Model):
   id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
   name = models.CharField(max_length=200)
   description = models.TextField(null=True, blank=True)
   participants = models.ManyToManyField(User, blank=True, related_name="events")
   start_date = models.DateTimeField()
   end_date = models.DateTimeField(null=True)
   registration_deadline = models.DateTimeField(null=True)
   createdAt = models.DateTimeField(auto_now_add=True)
   updatedAt = models.DateTimeField(auto_now=True)
   
   def __str__(self) -> str:
      return self.name

class Submission(models.Model):
   id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
   participant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="submissions")
   event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
   details = models.TextField(null=True, blank=True)
   
   def __str__(self) -> str:
      return f"{self.event} :x: {self.participant}"

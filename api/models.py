from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Transportation(models.Model):
    sender = models.ForeignKey(to=User, related_name = "sent_transportations", on_delete=models.CASCADE)
    receiver = models.ForeignKey(to=User, related_name = "receiver_transportations",  on_delete=models.CASCADE)
    file = models.FileField(upload_to='collections/')
    size = models.PositiveIntegerField()
    sent_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
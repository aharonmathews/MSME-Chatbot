from django.db import models

# Create your models here.
from django.db import models

class ChatMessage(models.Model):
    user_input = models.CharField(max_length=100)
    response = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth import get_user_model





User =get_user_model()
class Message(models.Model):
    sender=models.ForeignKey(User, related_name="sender",on_delete=models.CASCADE)
    receiver=models.ForeignKey(User, related_name="receiver",on_delete=models.CASCADE)
    message=models.CharField(max_length=5000,)
    seen=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id']
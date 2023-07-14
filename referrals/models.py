from django.db import models
from django.contrib.auth.models import User

# Referral Model with a User as a Foreign Key
class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=30, unique=True)
    used_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='used_referrals')
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from datetime import datetime


class CustomerSupport(models.Model):
    name = models.CharField(max_length=60, null=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    customer_email = models.CharField(max_length=32, null=False)
    subject = models.CharField(max_length=50, null=False)
    issue_description = models.TextField(null=False)
    date_time = models.CharField(max_length=20, blank=True)
    sent = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    

    def __str__(self):
        return f"[{self.name}] - {self.subject}"

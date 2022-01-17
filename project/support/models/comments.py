from django.db import models
from . import user, customer_support

class Comments(models.Model):
    text = models.CharField(max_length=200, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user.User, on_delete=models.CASCADE)
    customer_support = models.ForeignKey(customer_support.CustomerSupport, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}"
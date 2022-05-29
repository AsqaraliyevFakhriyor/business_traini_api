from django.db import models


class ApplicationModel(models.Model):
    username = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=250)
    email = models.CharField(max_length=200)
    business_type = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    visited = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.username

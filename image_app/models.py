from django.db import models

class Images(models.Model):
    image = models.ImageField(upload_to="img/", blank=False, null=False)
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)


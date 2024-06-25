from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=250, default="")
    phone = models.IntegerField(max_length=11, blank=True)
    bio = models.TextField(blank=True)
    image = ResizedImageField(
        size=[300, None],
        quality=70,
        upload_to="images/",
        default="../default_profile_gkgfzj",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"
from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name="profiles")
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.content

from django.db import models
from django.contrib.auth.models import User


LOCATION_OPTIONS = (
    ('Greece', 'GREECE'),
    ('Spain', 'SPAIN'),
    ('Italy', 'ITALY'),
    ('England', 'ENGLAND'),
)

THEME_OPTIONS = (
    ('Beach', 'BEACH'),
    ('Barn', 'BARN'),
    ('Classic', 'CLASSIC'),
    ('Rustic', 'RUSTIC'),
    ('Fairytale', 'FAIRYTALE'),
)

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    location = models.TextField(max_length=7, choices=LOCATION_OPTIONS, default='')
    theme = models.CharField(max_length=9, choices=THEME_OPTIONS, default='')
    image = models.ImageField(
        upload_to='images/', default='../default_post_a0da7q', blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
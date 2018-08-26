from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    institute = models.CharField(max_length=500, blank=True)
    rol = models.CharField(max_length=50, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username

from django.db import models

class Subscriber(models.Model):

    name_user=models.CharField(max_length=128)
    email_user = models.EmailField(max_length=70)

    def __str__(self):
        return self.email_user

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

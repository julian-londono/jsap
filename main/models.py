from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import HStoreField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='default@gmail.com')
    first = models.CharField(max_length=255, default='First')
    last = models.CharField(max_length=255, default='Last')
    birth_date = models.DateField(null=True, blank=True)
    fields_of_expertise = HStoreField(null=True)
    account_value = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    hours_taught = models.IntegerField(default=0)
    ratingsArray = ArrayField(models.IntegerField(default=0),null=True)
    avg_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, null=True)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

from django.utils import timezone
from django.db import models
from django.conf import settings
from coins.models import Coin

# subscription model
class Subscription(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, #'auth.User', 
                                related_name='subscription', 
                                on_delete=models.CASCADE,
                                blank=True)
    
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, unique=True)

    # last_updated = models.FloatField(default=-1)
    created = models.DateTimeField(default=timezone.now)
    
    def __unicode__(self):
        return self.coin
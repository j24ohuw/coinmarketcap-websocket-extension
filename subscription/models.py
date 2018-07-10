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
    
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    # last_updated = models.FloatField(default=-1)z
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = (
            ("owner", "coin")
        )
    def __unicode__(self):
        return self.coin

    def __str__(self):
        return self.coin.slug
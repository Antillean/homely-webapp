from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Charity(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "charities"

    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True, upload_to='user/photo')

    class Meta:
        abstract = True

class Receiver(User):
    beacon_id = models.CharField(max_length=100, unique=True)
    charity = models.ForeignKey(Charity)
    info = models.TextField(blank=True, null=True)
    amount_received = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    amount_targeted = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def amount_remaining(self):
        difference = amount_targeted - amount_received
        if difference <= 0:
            return 0
        else:
            return difference

    def __unicode__(self):
        return "%s (%s)" %(self.name, self.beacon_id)

class Giver(User):
    facebook_id = models.CharField(max_length=100, unique=True)
    amount_given = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __unicode__(self):
        return "%s (%s)" %(self.name, self.facebook_id)

class Donation(models.Model):
    giver = models.ForeignKey(Giver)
    receiver = models.ForeignKey(Receiver)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_token = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u"%s - \xA3%.2f -> %s" %(self.giver, self.amount, self.receiver)

## TODO: This logic is only guaranteed to work well for new donations.
## TODO: Edited donations will mess up giver and receiver totals.
## TODO: Also, put this where it should be!
@receiver(post_save, sender=Donation)
def update_receiver_and_giver_models_after_donation(sender, **kwargs):
    donation = kwargs.get('instance')

    receiver = donation.receiver
    receiver.amount_received += donation.amount
    receiver.save()

    giver = donation.giver
    giver.amount_given += donation.amount
    giver.save()

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class DateAware(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created']

class Charity(DateAware):
    name = models.CharField(max_length=100)

    class Meta(DateAware.Meta):
        verbose_name_plural = "charities"

    def __unicode__(self):
        return self.name

class Donation(DateAware):
    giver = models.ForeignKey('Giver')
    receiver = models.ForeignKey('Receiver')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_token = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u"%s - \xA3%.2f -> %s" %(self.giver, self.amount, self.receiver)

class User(DateAware):
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True, upload_to='user/photo')

    class Meta(DateAware.Meta):
        abstract = True

class Receiver(User):
    beacon_id = models.CharField(max_length=100, unique=True)
    charity = models.ForeignKey(Charity)
    info = models.TextField(blank=True, null=True)
    amount_received = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    amount_targeted = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def amount_remaining(self):
        difference = self.amount_targeted - self.amount_received
        if difference <= 0:
            return 0
        else:
            return difference

    @property
    def donations(self):
        return Donation.objects.filter(receiver=self)

    @property
    def givers(self):
        return [ donation.giver for donation in Donation.objects.filter(receiver__beacon_id=self.beacon_id) ]

    def __unicode__(self):
        return "%s (%s)" %(self.name, self.beacon_id)

class Giver(User):
    facebook_id = models.CharField(max_length=100, unique=True)
    amount_given = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    @property
    def donations(self):
        return Donation.objects.filter(giver=self)

    @property
    def receivers(self):
        return [ donation.receiver for donation in Donation.objects.filter(giver__facebook_id=self.facebook_id) ]

    def __unicode__(self):
        return "%s (%s)" %(self.name, self.facebook_id)


## TODO: Put this where it should be!
## TODO: Also, if you REALLY have time, make this properly transactional!
@receiver(pre_save, sender=Donation)
def update_receiver_and_giver_models_after_donation(sender, **kwargs):
    donation = kwargs.get('instance')
    update_amount = donation.amount

    ## If is update, update_amount is only difference between two amounts
    if donation.pk:
        old_amount = Donation.objects.get(pk=donation.pk).amount
        update_amount = donation.amount - old_amount

    receiver = donation.receiver
    receiver.amount_received += update_amount
    receiver.save()

    giver = donation.giver
    giver.amount_given += update_amount
    giver.save()

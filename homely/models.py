from django.db import models

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

    def __unicode__(self):
        return "%s (%s)" %(self.name, self.beacon_id)

class Giver(User):
    facebook_id = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return "%s (%s)" %(self.name, self.facebook_id)

class Donation(models.Model):
    giver = models.ForeignKey(Giver)
    receiver = models.ForeignKey(Receiver)
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    payment_token = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u"%s - \xA3%.2f -> %s" %(self.giver, self.amount, self.receiver)

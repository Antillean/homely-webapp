from django.db import models

class Charity(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "charities"

class User(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True, upload_to='user/photo')

    class Meta:
        abstract = True

class Receiver(User):
    facebook_id = models.CharField(max_length=100)
    charity = models.ForeignKey(Charity)
    info = models.TextField()

class Giver(User):
    beacon_id = models.CharField(max_length=100)

class Donation(models.Model):
    giver = models.ForeignKey(Giver)
    receiver = models.ForeignKey(Receiver)
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    payment_token = models.CharField(max_length=100)

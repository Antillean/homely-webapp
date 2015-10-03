from django.contrib import admin

from homely.models import Giver, Receiver, Donation, Charity

# Register your models here.
admin.site.register(Giver)
admin.site.register(Receiver)
admin.site.register(Donation)
admin.site.register(Charity)

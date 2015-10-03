from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from homely.rest.view_sets import ReceiverViewSet, DonationViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'receivers', ReceiverViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

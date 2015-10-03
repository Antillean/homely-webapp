from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from homely.rest.view_sets import ReceiverViewSet, DonationViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'receivers', ReceiverViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

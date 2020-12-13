from django.urls import path, include

from django.contrib import admin

import iotplug.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/


urlpatterns = [
    path("", include(router.urls)),
    path("qr", iotplug.views.qr),
    path("control", iotplug.views.control),
]

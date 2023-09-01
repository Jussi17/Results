from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('futis.urls', namespace='futis')),
    path('hoki/',include('hoki.urls', namespace='hoki')),
    path('koris/',include('koris.urls', namespace='koris')),
    path('golf/',include('golf.urls', namespace='golf')),
    path('faqs/',include('faqs.urls', namespace='faqs')),
    path('f1/',include('f1.urls', namespace='f1')),
]

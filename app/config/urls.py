from django.contrib import admin
from django.urls import path, include
from appointments.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('', home_view, name='home'),
    path('users/', include('users.urls', namespace='users')),  # Si tienes app users
]

from django.urls import path
from .views import (
    TodayAppointmentsListView,
    AppointmentListView,
    AppointmentCreateView,
    AppointmentDetailView,
    AppointmentUpdateView,
    AppointmentDeleteView,
)

app_name = 'appointments'  # Esto define el namespace

urlpatterns = [
    path('', TodayAppointmentsListView.as_view(), name='today'),
    path('list/', AppointmentListView.as_view(), name='list'),
    path('create/', AppointmentCreateView.as_view(), name='create'),
    path('<int:pk>/', AppointmentDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', AppointmentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', AppointmentDeleteView.as_view(), name='delete'),
]

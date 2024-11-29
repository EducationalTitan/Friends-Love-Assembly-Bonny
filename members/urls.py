# members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='events'),  # List of all events
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),  # Detailed view of a single event
    path('events/<int:event_id>/rsvp/', views.event_rsvp, name='event_rsvp'),
    path('success/', views.success, name='success'),
]

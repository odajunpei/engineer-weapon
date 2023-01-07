from django.urls import path
from . import views

app_name = 'studytime'

urlpatterns = [
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path('mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'
         ),
    path('mycalendar/<int:pk>/update', views.MyCalendarUpdate.as_view(), name='mycalendar_update'
         ),
]

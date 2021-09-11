from django.conf.urls import url
from fourth_app import views

app_name = 'fourth_app'

urlpatterns = [
    url('relative/',views.relative,name='relative'),
    url('other/',views.other,name = 'other'),
]

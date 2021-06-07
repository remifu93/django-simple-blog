from django.urls import path
from .views import HomeListView, HomeDetailView

app_name = 'home'

urlpatterns = [
    path('', HomeListView.as_view(), name='list'),
    path('post/<pk>', HomeDetailView.as_view(), name='detail'),
]
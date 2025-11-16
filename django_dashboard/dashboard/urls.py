from django.urls import path
from .views import home, ClientListView, ClientCreateView

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/new/', ClientCreateView.as_view(), name='client_create'),
]

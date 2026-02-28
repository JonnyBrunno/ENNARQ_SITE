from django.urls import path
from Construtora_ENAARQ.views import index

urlpatterns = [
    path('', index, name='index'),
]


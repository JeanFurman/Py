from django.urls import path
from myproject.core import views as v

urlpatterns = [
    path('', v.index, name='index'),
]
from django.urls import path
from .import views
urlpatterns = [
    path('', views.finacial_summary, name='financial_summary')
]
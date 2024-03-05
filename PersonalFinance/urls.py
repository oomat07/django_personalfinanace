from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.Incomes.urls')),
    path('', include('apps.Expenses.urls')),
    path('', include('apps.Analytics.urls'))
]

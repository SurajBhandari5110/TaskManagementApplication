from django.contrib import admin
from django.urls import path
from TMA import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('TMA.urls')),
    path('api/', include('TMA.urls')),

]

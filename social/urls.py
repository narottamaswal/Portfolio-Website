from django.contrib import admin
from django.urls import path,include

urlpatterns = [
 #   path('api-auth/', include('rest_framework.urls')),
  #  path('api/', include('firstapp.api.urls')),
    path('',include('portfolio.urls')),
    path('admin/', admin.site.urls),
]

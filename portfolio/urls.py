from django.urls import path
from .views import index,download_file

urlpatterns=[
    path('',index,name="index"),    path('download/', download_file),

]

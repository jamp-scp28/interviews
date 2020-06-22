from django.urls import path, include
from . import views

urlpatterns = [
    path('appl_form/', views.appl_form,name='appl_insert'), # get and post req. for insert operation
    path('appl_list/',views.appl_list,name='appl_list'), # get req. to retrieve and display all records
]
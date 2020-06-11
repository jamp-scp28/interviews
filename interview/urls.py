from django.urls import path, include
from . import views

urlpatterns = [
    path('int_main_form/', views.int_form,name='int_insert'), # get and post req. for insert operation
    path('int_update/<int:id>/', views.int_form,name='int_update'), # get and post req. for update operation
    path('int_delete/<int:id>/',views.int_delete,name='int_delete'),
    path('int_list/',views.int_list,name='int_list'), # get req. to retrieve and display all records
]
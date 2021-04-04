from django.conf.urls import url
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from demo import views  #Import the views from the demo folder to get the index action

urlpatterns = [
    path('', views.user_form,name='user_insert'), # get and post req. for insert operation
    path('<int:id>/', views.user_form,name='user_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.user_delete,name='user_delete'),
    path('list/',views.user_list,name='user_list') # get req. to retrieve and display all records
]
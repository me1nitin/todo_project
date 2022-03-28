from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:p_id>/', views.updates, name='update'),
    path('cbvlistview/', views.Tasklistview.as_view(), name='cbvlistview'),
    path('cbvdetail/<int:pk>/', views.Taskdetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Taskdelete.as_view(), name='cbvdelete'),
]

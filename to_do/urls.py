from django.urls import path
from . import views,api

urlpatterns =  [
    
    path('' ,views.do , name = 'list'),
    path('add_task',views.addTask,name="add_task"),
    path('update_task/<str:pk>/',views.updateTask,name='update_task'),
    path('delete_task/<str:pk>/',views.deleteTask,name='delete_task'),
    path('task_details/<str:pk>/',views.taskDetails,name='task_details'),
    path('api/tasks',api.task_list_api,name='task_list_api'),
    path('api/task/<str:pk>/',api.task_detail_api,name='task_detail_api'),
    path('api/v2/tasks/',api.TasksCreateApi.as_view(),name='TasksCreateApi'),
    path('api/v2/task/<str:pk>/',api.TaskDetail.as_view(),name='TaskDetail'),

]

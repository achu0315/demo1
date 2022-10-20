from . import views
from django.urls import path
app_name='appname'

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('detail',views.detail,name='detail')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('home/',views.tasklist.as_view(),name='home'),
    path('detail/<int:pk>',views.taskdetail.as_view,name='detail'),
     path('up/<int:pk>',views.taskupdate.as_view,name='up'),
    path('del/<int:pk>',views.taskdelete.as_view,name='del'),
]

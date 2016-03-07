from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tasks/$', views.TaskList.as_view(), name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view(), name='task_detail'),
]

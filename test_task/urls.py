from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_of_users, name='index'),
    url(r'^download/', views.download_list, name='download'),
    url(r'^register/', views.create_user, name='register'),
    url(r'^edit/', views.edit_user, name='edit'),
    url(r'^view/', views.view_user, name='view'),
    url(r'^login/', views.log_in, name='login')
]

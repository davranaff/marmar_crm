from django.urls import path

from . import views


urlpatterns = [
    path('', views.login_user, name="login_user"),
    path('home', views.index, name="home"),
    path('clients', views.clients, name="clients"),
    path('edit_client/<int:pk>', views.edit_client, name="edit_client_pk"),
    path('offic/', views.offic, name="offic"),
    path('edit_offic/<int:pk>', views.edit_offic, name="edit_offic_pk"),
    path('department_<pk>/', views.department, name="department"),
    path('service', views.service, name="service"),
    path('archive/<int:pk>', views.archive, name="archive_pk"),
    path('log_out', views.sign_out, name="sign_out"),
    path('edit_percent_<pk>/', views.edit_percent, name='edit_percent')
]

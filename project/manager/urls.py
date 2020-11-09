from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.homepage, name='home'),
    path('password_change/', views.password_change, name='password_change'),
    path('services/adding_report/', views.adding_report, name='adding_report'),
    path('services/searching_client/', views.searching_client, name='searching_client'),
    path('services/searching_report/', views.searching_report, name='searching_report'),

]


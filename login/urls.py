from django.urls import path
from . import views

urlpatterns = [
    #path('',views.login_cure, name="login"),
    path('redirectapp', views.appredirect, name="redirectapp"),
    path('redirectGHP', views.appredirectGHP, name="redirect"),
    path('csvdatadownload', views.login_admin, name="loginadmin")
]

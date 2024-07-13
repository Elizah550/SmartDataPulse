from django.urls import path
from . import views
from .views import *

urlpatterns = [
    #path('', views.homepage, name="homepage"),
    path('', views.cure_trial, name='cure_trial'),
    path('Wearables', views.cure_test_trial, name='Wearables'),
    path('GHPWearables', views.GHP_Wearables, name='GHP_Wearables'),
    #path('Wearables', views.Wearables, name='Wearables'),
    path('toc', views.toc, name='toc'),
    path('app/privacy', views.privacy, name='privacy'),
    path('privacy', views.privacyweb, name='privacyweb'),
    path('apple-app-site-association', views.myappleunilink, name="aasa"),
    #path('logout', views.logout, name="logout"),
    #path('intraday', views.intradaypage, name="intradaypage"),
    #path('profile', views.profile, name="profile"),
    #path('wearables', views.wearables, name="wearables"),
    #path('admincsvdata', views.csvdownloader, name="csvdata"),
    path('admindownloaddata', views.csvcreator, name="csvdld"),
    #path('ajax', ajaxHandlerView.as_view()),
    #path('ajaxintraday', intradayAjaxHandlerView.as_view()),
    path('gateway_post', views.gateway_post, name="gateway_post"),
]

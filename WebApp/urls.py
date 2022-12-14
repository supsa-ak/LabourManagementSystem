from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),   
    path('profile', views.profile, name='profile'),   
    path('user', views.user, name='user'),   
    path('signup', views.signup, name='signup'),
    path('contact', views.contact, name='contact'),
    path('request-labour', views.requestLabour, name='request-labour'),
    path('request2', views.request2, name='req2'),
    path('payment', views.payment, name='payment'),
    path('done', views.done, name='done'),
]
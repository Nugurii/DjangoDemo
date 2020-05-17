from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('user/signin', views.Signin.as_view(), name='signin'),
    path('user/signup', views.Signup.as_view(), name='signup'),
    path('user/logout', views.Logout.as_view(), name='logout'),
]
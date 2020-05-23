from django.urls import path
from myapp import views
# from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
    path('token-verify', views.TokenVerifyView.as_view(), name='token-verify'),
    path('home', views.HomeView.as_view(), name='home'),
    path('user/signin', views.SigninView.as_view(), name='signin'),
    path('user/signup', views.SignupView.as_view(), name='signup'),
    path('user/logout', views.LogoutView.as_view(), name='logout'),
]
from django.urls.conf import path
from useraccounts.views import RegisterAPIView,LoginAPIView, UserListAPIView
from . import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name = "register"),
    path('login/', views.LoginAPIView.as_view(), name = "login"),
]
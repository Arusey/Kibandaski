from django.urls import path
from django.conf.urls import url
from .views import CreateUserAPIView, LoginUser, VerifyEmailAPIView


urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('login/', LoginUser.as_view()),
    path('verify/<token>/', VerifyEmailAPIView.as_view())
]

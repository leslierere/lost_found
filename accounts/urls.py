from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', LoginView.as_view(), name = 'login_urlpattern'),
    path('register/', views.register, name = 'register'),
    path('logout', LogoutView.as_view(next_page = 'index'), name = 'logout_urlpattern'),
]

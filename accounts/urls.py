from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', LoginView.as_view(), name = 'login_urlpattern'),
    path('logout', LogoutView.as_view(next_page = 'login_urlpattern'), name = 'logout_urlpattern'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.view_profile, name = 'view_profile'),
    path('profile/edit/', views.edit_profile, name = 'edit_profile'),
    path('change-password/', views.change_password, name = 'change_password'),
]

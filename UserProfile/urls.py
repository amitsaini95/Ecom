from django.urls import path
from .import views
app_name="auth"
urlpatterns=[
    path('Signup',views.SignUpView,name="Signup"),
    path('Login',views.LoginView,name="Login"),
    path('Logout',views.LogoutView,name="Logout"),



]
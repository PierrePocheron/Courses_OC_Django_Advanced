"""fotoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

import authentification.views
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Url via vue générique
    path('', LoginView.as_view(
            template_name='authentification/login.html',
            redirect_authenticated_user=True),
            name='login'),

    # Url via vue basée sur une Classe
    # path('', authentification.views.LoginPageView.as_view(), name='login'),

    # Url via vue basée sur une Fonction
    # path('', authentification.views.login_page, name="login"),

    #  Url via vue générique
    path('logout/', LogoutView.as_view(
            template_name='blog/home.html'),
            name='logout'),

    # Url via fonction
    # path('logout/', authentification.views.logout_user, name='logout'),

    #  Url via vue générique
    path('changePassword/', PasswordChangeView.as_view(
            template_name='authentification/password_change_form.html'),
            name='changePassword'),

    #  Url via vue générique
    path('changePasswordDone/', PasswordChangeDoneView.as_view(
            template_name='authentification/password_change_done.html'),
            name='changePasswordDone'),

    path('signup/', authentification.views.signup_page, name='signup'),

    path('home/', blog.views.home, name='home'),
]

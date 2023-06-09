"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from web_revenue.views import upload_csv, sign_in, update_name, upload_from_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('revenue/', upload_csv, name='revenue'),
    path('form_revenue/', upload_from_form, name='form-revenue'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign_in/', sign_in, name='sign-in'),
    path('profile/', update_name, name='profile'),
]
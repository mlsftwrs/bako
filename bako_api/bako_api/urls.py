"""
URL configuration for bako_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account_creation/", views.create_account),
    path("login/", views.login),
    path("change_username/", views.change_username),
    path("change_password/", views.change_password),
    path("account_deletion/", views.account_deletion),
    path("book/", views.get_book_endpoint),
    path("catalog/", views.catalog),
    path("bookmark/", views.mark_book_as_inprogress),
    path("book_completed/", views.book_completed),
    path("calculate_score/", views.score_calculation),
    path("user/", views.get_user_data_endpoint),
]

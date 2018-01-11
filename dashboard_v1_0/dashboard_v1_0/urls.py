"""dashboard_v1_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from interface import views as interface_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r"^product/$", views.ProductPage.as_view(), name="product"),
    url(r"^solutions/$", views.SolutionsPage.as_view(), name="solutions"),
    url(r"^industries/$", views.IndustriesPage.as_view(), name="industries"),
    url(r"^demo/$", views.DemoPage.as_view(), name="demo"),
    url(r"^about/$", views.AboutPage.as_view(), name="about"),
    url(r"^contact_us/$", views.ContactUsPage.as_view(), name="contact_us"),
    url(r"login/$", auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r'^interface/',include('interface.urls',namespace='interface')),
    url(r'^dashboard/$',interface_views.DashboardPage.as_view(),name='dashboard'),
]

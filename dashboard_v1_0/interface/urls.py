from django.conf.urls import url, include
from interface import views

urlpatterns = [
    url(r"^reports/$", views.ReportsPage.as_view(), name="reports"),
    url(r"^dashboard/$", views.DashboardPage.as_view(), name="dashboard"),
    url(r"^forecasts/$", views.ForecastsPage.as_view(), name="forecasts"),
    url(r"^optimization/$", views.OptimizationPage.as_view(), name="optimization"),
]

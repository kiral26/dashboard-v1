from django.conf.urls import url, include
from interface import views

urlpatterns = [
    url(r"^reports_sales/$", views.ReportsSalesPage.as_view(), name="reports_sales"),
    url(r"^reports_costs/$", views.ReportsCostsPage.as_view(), name="reports_costs"),
    url(r"^reports_inventory/$", views.ReportsInventoryPage.as_view(), name="reports_inventory"),
    url(r"^dashboard/$", views.DashboardPage.as_view(), name="dashboard"),
    url(r"^forecasts/$", views.ForecastsPage.as_view(), name="forecasts"),
    url(r"^optimization/$", views.OptimizationPage.as_view(), name="optimization"),
]

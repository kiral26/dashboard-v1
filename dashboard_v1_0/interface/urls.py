from django.conf.urls import url, include
from interface import views

urlpatterns = [
    url(r"^reports_sales/$", views.ReportsSalesPage.as_view(), name="reports_sales"),
    url(r"^reports_costs/$", views.ReportsCostsPage.as_view(), name="reports_costs"),
    url(r"^reports_inventory/$", views.ReportsInventoryPage.as_view(), name="reports_inventory"),
    url(r"^dashboard/$", views.DashboardPage.as_view(), name="dashboard"),
    url(r"^forecasts_sales/$", views.ForecastsSalesPage.as_view(), name="forecasts_sales"),
    url(r"^forecasts_costs/$", views.ForecastsCostsPage.as_view(), name="forecasts_costs"),
    url(r"^forecasts_inventory/$", views.ForecastsInventoryPage.as_view(), name="forecasts_inventory"),
    url(r"^optimize_sales/$", views.OptimizeSalesPage.as_view(), name="optimize_sales"),
    url(r"^optimize_costs/$", views.OptimizeCostsPage.as_view(), name="optimize_costs"),
    url(r"^optimize_inventory/$", views.OptimizeInventoryPage.as_view(), name="optimize_inventory"),
]

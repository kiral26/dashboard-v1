from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ReportsSalesPage(TemplateView):
    template_name = "interface/reports_sales.html"

class ReportsCostsPage(TemplateView):
    template_name = "interface/reports_costs.html"

class ReportsInventoryPage(TemplateView):
    template_name = "interface/reports_inventory.html"

class DashboardPage(TemplateView):
    template_name = "interface/dashboard.html"

class ForecastsPage(TemplateView):
    template_name = "interface/forecasts.html"

class OptimizationPage(TemplateView):
    template_name = "interface/optimization.html"

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

class ForecastsSalesPage(TemplateView):
    template_name = "interface/forecasts_sales.html"

class ForecastsCostsPage(TemplateView):
    template_name = "interface/forecasts_costs.html"

class ForecastsInventoryPage(TemplateView):
    template_name = "interface/forecasts_inventory.html"

class OptimizeSalesPage(TemplateView):
    template_name = "interface/optimize_sales.html"

class OptimizeCostsPage(TemplateView):
    template_name = "interface/optimize_costs.html"

class OptimizeInventoryPage(TemplateView):
    template_name = "interface/optimize_inventory.html"

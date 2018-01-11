from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ReportsPage(TemplateView):
    template_name = "interface/reports.html"

class DashboardPage(TemplateView):
    template_name = "interface/dashboard.html"

class ForecastsPage(TemplateView):
    template_name = "interface/forecasts.html"

class OptimizationPage(TemplateView):
    template_name = "interface/optimization.html"

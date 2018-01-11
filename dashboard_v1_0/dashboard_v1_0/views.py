from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("dashboard"))
        return super().get(request, *args, **kwargs)

class ProductPage(TemplateView):
    template_name = "product.html"

class SolutionsPage(TemplateView):
    template_name = "solutions.html"

class IndustriesPage(TemplateView):
    template_name = "industries.html"

class DemoPage(TemplateView):
    template_name = "demo.html"

class AboutPage(TemplateView):
    template_name = "about.html"

class ContactUsPage(TemplateView):
    template_name = "contact_us.html"

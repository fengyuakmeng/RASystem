from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "base/system_base.html"


class IndexView(TemplateView):
    template_name = "RASystem/index.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

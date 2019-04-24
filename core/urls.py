from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        "nosotros/",
        TemplateView.as_view(template_name="nosotros.html"),
        name="nosotros",
    ),
    path(
        "soluciones/",
        TemplateView.as_view(template_name="soluciones.html"),
        name="soluciones",
    ),
    path(
        "experiencia/",
        TemplateView.as_view(template_name="experiencia.html"),
        name="experiencia",
    ),
    path(
        "contacto/",
        TemplateView.as_view(template_name="contacto.html"),
        name="contacto",
    ),
    path(
        "",
        TemplateView.as_view(template_name="home.html"),
        name="home",
    ),
]
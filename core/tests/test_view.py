from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Home')

    def test_nosotros_page_works(self):
        response = self.client.get(reverse("nosotros"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nosotros.html')
        self.assertContains(response, 'Nosotros')

    def test_soluciones_page_works(self):
        response = self.client.get(reverse("soluciones"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'soluciones.html')
        self.assertContains(response, 'Soluciones')

    def test_experiencia_page_works(self):
        response = self.client.get(reverse("experiencia"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experiencia.html')
        self.assertContains(response, 'Experiencia')

    def test_contacto_page_works(self):
        response = self.client.get(reverse("contacto"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacto.html')
        self.assertContains(response, 'Contacto')
from django.test import TestCase
from authentication.forms import SignUpWithCodeForm

# Create your tests here.
class SignUpWithCodeFormTest(TestCase):
    def test_form(self):
        form = SignUpWithCodeForm()
        self.assertTrue(form.is_valid())
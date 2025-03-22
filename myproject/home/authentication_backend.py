from django.contrib.auth.backends import BaseBackend
from .models import registration_data

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = registration_data.objects.get(email=username)  # Use email as username
            if user.check_password(password):
                return user
        except registration_data.DoesNotExist:
            return None

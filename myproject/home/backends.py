from django.contrib.auth.backends import BaseBackend
from .models import registration_data

class CustomBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = registration_data.objects.get(email=email)
            if user.check_password(password):
                return user
        except registration_data.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return registration_data.objects.get(pk=user_id)
        except registration_data.DoesNotExist:
            return None

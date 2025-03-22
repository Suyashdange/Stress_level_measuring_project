from django.contrib import admin
#showing database data in admin panel 
from home.models import *

admin.site.register(registration_data)
admin.site.register(StressAssessmentResponse)
admin.site.register(test_data)
admin.site.register(appointement_data)
admin.site.register(counsellor_data)
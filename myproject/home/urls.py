from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('counsellor/', views.counsellor_view, name='counsellor'),
    path('appointment/', views.appointment_view, name='appointment'),
    path('accept/', views.accept, name='accept'),
    path('reject/', views.reject, name='reject'),
    path('counsellors/', views.counsellors_view, name='counsellors'),
    path('stress-assessment/', views.stress_assessment_view, name='stress-assessment'),
    path('test_view/', views.test_view, name='test-view')

]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
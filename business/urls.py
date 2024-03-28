from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('1961925e-a798-4bc6-85d8-adff44b55836/', views.whatsappWebhook, name='whatsapp-webhook'),
]

# CallbackURL = 'https:://rajesh3110.pythonanywhere.com/1961925e-a798-4bc6-85d8-adff44b55836'
# Verify Token = '3769a501-51d1-432e-873e-1c223dc3bcb7'
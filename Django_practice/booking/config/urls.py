from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doc/', get_swagger_view(title='Booking API Manual')),
    path('api/get_token/', views.obtain_auth_token),
    path('', include('booking.urls')),
]
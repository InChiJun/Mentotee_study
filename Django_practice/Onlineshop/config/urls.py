from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('order/', include('order.urls')),
    path('coupon/', include('coupon.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]
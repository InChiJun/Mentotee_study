from django.urls import path
from .views import *
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'orders'

urlpatterns = [
    path('admin_order_detail/<int:order_id>/', staff_member_required(admin_order_detail), name='admin_order_detail'),
    path('create/', order_create, name='order_create'),
    path('create_ajax/', OrderCreateAjaxView.as_view(), name='order_create_ajax'),
    path('checkout/', OrderCheckoutAjaxView.as_view(), name='order_checkout'),
    path('validation/', OrderImAjaxView.as_view(), name='order_validation'),
    path('complete/', order_complete, name='order_complete'),
]
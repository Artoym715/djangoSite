from django.urls import path
from .views import index
from .views import basket, sorted_basket, product_update_form, product_update_id_form



urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('user/<int:user_id>/', basket, name='basket'),
    path('user_sorted/<int:user_id>/<int:days_ago>/', sorted_basket, name='sorted_basket'),
    path('product_update/<int:product_id>', product_update_form, name='product_update'),
    path('product_update_id/', product_update_id_form, name='product_update_id'),


]
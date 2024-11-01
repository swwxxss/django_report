from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from .views import home, register, your_view, book_list, book_detail, book_create, book_update, book_delete, add_to_cart, remove_from_cart, cart_view, search_books, login_view, profile_view, checkout, order_success, process_order

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='library/login.html'), name='login'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('books/', book_list, name='book_list'),
    # path('', book_list, name='book_list'),
    path('cart/', cart_view, name='cart_view'),
    path('remove_from_cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
    path('register/', register, name='register'),
    path('search/', search_books, name='search_books'),
    path('book/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('your-view/', your_view, name='your_view'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('book/new/', book_create, name='book_create'),
    # path('book/<int:pk>/info/', book_info, name='book_info'),
    path('book/<int:pk>/edit/', book_update, name='book_update'),
    path('book/<int:pk>/delete/', book_delete, name='book_delete'),
    path('checkout/', checkout, name='checkout'),
    path('order_success/', lambda request: render(request, 'order_success.html'), name='order_success'),
    path('order-success/', order_success, name='order_success'),
    path('checkout/', checkout, name='checkout'),
    path('process_order/', process_order, name='process_order'),
]

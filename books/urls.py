from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from library.views import *
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('library.urls')),
    path('login/', login, name='login'),  # ваш маршрут для входу
    path('register/', register, name='register'),
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('search/', search_books, name='search_books'),
    path('cart/', cart_view, name='cart_view'),
    path('remove_from_cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
    path('library/', include('library.urls')),
    path('books/', book_list, name='book_list'),
    path('products/', product_list, name='product_list'),
    path('books/', book_list, name='book_list'),
    path('library/', include('library.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





# from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from library.views import *
#
# urlpatterns = [
#     path('', home, name='home'),
#     path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
#     path('register/', register, name='register'),
#     path('books/', book_list, name='book_list'),
#     path('library/', include('library.urls')),
# ]